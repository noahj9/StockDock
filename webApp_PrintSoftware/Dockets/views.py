from django.shortcuts import render, redirect
from .forms import NewDocketForm
from django.http import HttpResponseRedirect,JsonResponse
import calendar
from calendar import HTMLCalendar
from .models import Docket, Contact
from .filters import DocketFilter
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django_addanother.views import CreatePopupMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ContactCreate(LoginRequiredMixin, CreatePopupMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Contact
    fields = ['name', 'phone', 'email', 'client']

def home(request): #passes dockets to the page and creates a query set which can be searched and filtered
    docket_list = Docket.objects.all()
    myFilter = DocketFilter(request.GET, queryset=docket_list)
    docket_list = myFilter.qs
    return render(request, 'dockets/home.html', {'docket_list': docket_list, 'myFilter': myFilter})

class CreateDocket(LoginRequiredMixin, CreatePopupMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Docket
    form_class = NewDocketForm
    def get_success_url(self):
        return reverse_lazy('dockets-home')

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
        docket.delete()
        return HttpResponseRedirect('/dockets')
    context = {'item':docket}
    return render(request, 'dockets/delete.html', context)

@login_required
def printDocket(request, pk):
    docket = Docket.objects.get(id=pk)


@login_required
def cloneDocket(request, pk):
    docket = Docket.objects.get(id=pk)
    docket.pk = None
    docket.save() #save form to DB\
    return redirect('dockets-home')

@login_required
def addJob(request, pk):
    docket = Docket.objects.get(id=pk)
    docket.pk = None
    docket.quantity_1 = ""
    docket.description_1 = ""
    docket.finished_size_1 = ""
    docket.stock_1 = None
    docket.machine = ""
    docket.run_quantity_1 = ""
    docket.sheet_size_1 = ""
    docket.run_size_1 = ""
    docket.proof_1 = None
    docket.inks_1 = None
    docket.instructions_1 = ""
    docket.bindery_1 = ""
    docket.file_1 = ""
    docket.price_comission_1 = ""
    docket.shipping_1 = ""
    docket.terms = None
    docket.save()
    return redirect('dockets-update', pk = docket.pk)


