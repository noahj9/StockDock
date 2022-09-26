from django.shortcuts import render
from .forms import NewDocketForm
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from .models import Docket
from .filters import DocketFilter
from django.contrib.auth.decorators import login_required

def home(request): #passes dockets to the page and creates a query set which can be searched and filtered
    docket_list = Docket.objects.all()
    myFilter = DocketFilter(request.GET, queryset=docket_list)
    docket_list = myFilter.qs
    return render(request, 'dockets/home.html', {'docket_list': docket_list, 'myFilter': myFilter})

@login_required
def newDocket(request): #new docket form view
    form = NewDocketForm()
    if request.method == "POST": #if the method is post then post the request to the DB
        form = NewDocketForm(request.POST)
        if form._is_valid(): #check for validity
            form.save() #save form to DB\
            return redirect('/')

    context = {'form':form}
    return render(request, 'dockets/new.html', context) #render the page

@login_required
def updateDocket(request, pk):
    docket = Docket.objects.get(id=pk)
    form = NewDocketForm(instance=docket)

    if request.method == "POST": #if the method is post then post the request to the DB
        form = NewDocketForm(request.POST, instance=docket)
        if form._is_valid(): #check for validity
            form.save() #save form to DB\
            return redirect('/')

    context = {'form':form}
    return render(request, 'dockets/new.html', context)

@login_required
def deleteDocket(request, pk):
    docket = Docket.objects.get(id=pk)
    if request.method =="POST":
        docket.delete()
    context = {'item':docket}
    return render(request, 'dockets/delete.html', context)


