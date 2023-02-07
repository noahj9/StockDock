import os
from django.shortcuts import render, redirect
from .forms import NewDocketForm
from django.http import FileResponse, HttpResponse, HttpResponseRedirect,JsonResponse
import calendar
from calendar import HTMLCalendar
from .models import Docket, Contact, Client, Stock, Ink, Proof
from .filters import DocketFilter
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django_addanother.views import CreatePopupMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
import Dockets.scripts.pdf_filler as filler
import json
import time

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
            print ("removed " + filename)
            os.remove('./Dockets/scripts/'+filename)
    return render(request, 'dockets/home.html', {'docket_list': docket_list, 'myFilter': myFilter})

class CreateDocket(LoginRequiredMixin, CreatePopupMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Docket
    form_class = NewDocketForm
    initial = {'inks_1': 'N/A'}
    def get_success_url(self):
        return reverse_lazy('dockets-home')

def updateSubCats(req): #update contact lists for email and phone number, via JS scripts
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

class UpdateDocket(LoginRequiredMixin, CreatePopupMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Docket
    form_class = NewDocketForm
    def get_initial(self):
        initial = super().get_initial()
        try:
            proof_1 = self.get_object().proof_1
            proof_2 = self.get_object().proof_2
            proof_3 = self.get_object().proof_3
            stock_1 = self.get_object().stock_1
            stock_2 = self.get_object().stock_2
            stock_3 = self.get_object().stock_3
            inks_1 = self.get_object().inks_1
            inks_2 = self.get_object().inks_2
            inks_3 = self.get_object().inks_3
            machine_1 = self.get_object().machine_1
            machine_2 = self.get_object().machine_2
            machine_3 = self.get_object().machine_3
        except:
            pass
        else:
            initial['proof_1'] = proof_1
            initial['proof_2'] = proof_2
            initial['proof_3'] = proof_3
            initial['stock_1'] = stock_1
            initial['stock_2'] = stock_2
            initial['stock_3'] = stock_3
            initial['inks_1'] = inks_1
            initial['inks_2'] = inks_2
            initial['inks_3'] = inks_3
            initial['machine_1'] = machine_1
            initial['machine_2'] = machine_2
            initial['machine_3'] = machine_3
        return initial
    def get_success_url(self):
       return reverse_lazy('dockets-home')
    


# @login_required
# def updateDocket(request, pk):
#     docket = Docket.objects.get(id=pk)
#     form = NewDocketForm(instance=docket)
#     #stock1 = Stock.objects.filter(name=docket.stock_1)


#     if request.method == "POST": #if the method is post then post the request to the DB
#         form = NewDocketForm(request.POST, instance=docket)
#         if form.is_valid(): #check for validity
#             form.save() #save form to DB\
#             return redirect('dockets-home')

#     context = {'form':form}
#     return render(request, 'dockets/docket_form.html', context)

@login_required
def deleteDocket(request, pk):
    docket = Docket.objects.get(id=pk)
    if request.method =="POST":
        docket.delete()
        return HttpResponseRedirect('/dockets')
    context = {'item':docket}
    return render(request, 'dockets/delete.html', context)

@login_required
def printDocket(req, pk):
    docket = Docket.objects.get(id=pk)
    client = docket.customer_name
    terms = docket.terms
    customer_po = docket.customer_PO
    deposit = docket.deposit
    rep = docket.rep
    csr = docket.csr
    contact = Contact.objects.get(name = docket.contact)
    path = filler.execute(model_to_dict(docket),model_to_dict(contact), client, terms, customer_po, deposit, rep, csr)
    reverse_lazy('dockets-home')
    return FileResponse(open(path, 'rb'),content_type='application/pdf')


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
    docket.quantity_1 = ""
    docket.description_1 = ""
    docket.finished_size_1 = ""
    docket.stock_1 = ""
    docket.machine = ""
    docket.run_quantity_1 = ""
    docket.sheet_size_1 = ""
    docket.run_size_1 = ""
    docket.proof_1 = ""
    docket.inks_1 = ""
    docket.instructions_1 = ""
    docket.bindery_1 = ""
    docket.file_1 = ""
    docket.price_comission_1 = ""
    docket.shipping_1 = ""
    docket.quantity_2 = ""
    docket.description_2 = ""
    docket.finished_size_2 = ""
    docket.stock_2 = ""
    docket.machine_2 = ""
    docket.run_quantity_2 = ""
    docket.sheet_size_2 = ""
    docket.run_size_2 = ""
    docket.proof_2 = ""
    docket.inks_2 = ""
    docket.instructions_2 = ""
    docket.bindery_2 = ""
    docket.file_2 = ""
    docket.price_comission_2 = ""
    docket.shipping_2 = ""
    docket.quantity_3 = ""
    docket.description_3 = ""
    docket.finished_size_3 = ""
    docket.stock_3 = ""
    docket.machine_3 = ""
    docket.run_quantity_3 = ""
    docket.sheet_size_3 = ""
    docket.run_size_3 = ""
    docket.proof_3 = ""
    docket.inks_3 = ""
    docket.instructions_3 = ""
    docket.bindery_3 = ""
    docket.file_3 = ""
    docket.price_comission_3 = ""
    docket.shipping_3 = ""
    docket.reception_notes = ""
    docket.save()
    return redirect('dockets-update', pk = docket.pk)


