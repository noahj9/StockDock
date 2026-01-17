import os
from django.shortcuts import render, redirect
from .forms import NewDocketForm
from django.http import FileResponse, HttpResponse, HttpResponseRedirect,JsonResponse
import calendar
from calendar import HTMLCalendar
from .models import Docket, Contact, Client, Stock, Ink
from .filters import DocketFilter
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django_addanother.views import CreatePopupMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
import Dockets.scripts.pdf_filler as filler
import json
import time
import logging

logger = logging.getLogger(__name__)

class ContactCreate(LoginRequiredMixin, CreatePopupMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Contact
    fields = ['name', 'phone', 'email', 'client']

class ClientCreate(LoginRequiredMixin, CreatePopupMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Client
    fields = ['name']


def home(request): #passes dockets to the page and creates a query set which can be searched and filtered
    docket_list = Docket.objects.all()
    myFilter = DocketFilter(request.GET, queryset=docket_list)
    docket_list = myFilter.qs
    for filename in os.listdir('./Dockets/scripts'):
        if "filled" in filename:
            try:
                os.remove('./Dockets/scripts/'+filename)
                logger.info(f"Deleted temporary PDF file: {filename}")
            except Exception as e:
                logger.error(f"Failed to delete temporary PDF file {filename}: {str(e)}")
    return render(request, 'dockets/home.html', {'docket_list': docket_list, 'myFilter': myFilter})

class CreateDocket(LoginRequiredMixin, CreatePopupMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Docket
    form_class = NewDocketForm
    def get_success_url(self):
        return reverse_lazy('dockets-home')

def updateSubCats(req):
    data = req.GET.get('name')
    result = Contact.objects.get(name__exact = data)
    responseObj = {
        "phone": result.phone,
        "email": result.email,
    }
    return HttpResponse(json.dumps(responseObj), content_type="application/json")


def getContacts(request):
    data = json.loads(request.body)
    client_Id = data["id"]
    contacts = Contact.objects.filter(client__id = client_Id)
    return JsonResponse(list(contacts.values("id", "name")), safe = False)

@login_required
def updateDocket(request, pk):
    docket = Docket.objects.get(id=pk)
    form = NewDocketForm(instance=docket)

    if request.method == "POST": #if the method is post then post the request to the DB
        form = NewDocketForm(request.POST, instance=docket)
        if form.is_valid(): #check for validity
            form.save() #save form to DB\
            return redirect('dockets-home')

    context = {'form':form}
    return render(request, 'dockets/docket_form.html', context)

@login_required
def deleteDocket(request, pk):
    docket = Docket.objects.get(id=pk)
    if request.method =="POST":
        logger.info(f"Deleting docket id {pk}")
        docket.delete()
        return HttpResponseRedirect('/dockets')
    context = {'item':docket}
    return render(request, 'dockets/delete.html', context)

@login_required
def printDocket(req, pk):
    docket = Docket.objects.get(id=pk)
    contact = Contact.objects.get(name = docket.contact)
    try:
        path = filler.execute(model_to_dict(docket),model_to_dict(contact))
        logger.info(f"Generated PDF for docket id {pk}")
        reverse_lazy('dockets-home')
        return FileResponse(open(path, 'rb'),content_type='application/pdf')
    except Exception as e:
        logger.critical(f"CRITICAL: Failed to generate pdf for docket id {pk}: {str(e)}")
        raise


@login_required
def cloneDocket(request, pk):
    docket = Docket.objects.get(id=pk)
    docket.pk = None
    docket.save() #save form to DB
    return redirect('dockets-home')

@login_required
def addJob(request, pk):
    docket = Docket.objects.get(id=pk)
    docket.pk = None

    # Define job field base names that repeat across sections 1, 2, and 3
    job_field_names = [
        'quantity', 'description', 'finished_size', 'stock', 'machine',
        'run_quantity', 'sheet_size', 'run_size', 'proof', 'inks',
        'instructions', 'bindery', 'file', 'price_comission', 'shipping'
    ]

    # Clear all job-specific fields across sections 1-3 using loops
    for section in range(1, 4):
        for field_name in job_field_names:
            field_attr = f"{field_name}_{section}"
            setattr(docket, field_attr, "")

    # Clear additional fields
    docket.reception_notes = ""

    docket.save()
    return redirect('dockets-update', pk = docket.pk)


