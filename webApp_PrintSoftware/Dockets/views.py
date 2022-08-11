from django.shortcuts import render
from .forms import NewDocketForm
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from .models import Docket
from .filters import DocketFilter

def home(request): #passes dockets to the page and creates a query set which can be searched and filtered
    docket_list = Docket.objects.all()
    myFilter = DocketFilter(request.GET, queryset=docket_list)
    docket_list = myFilter.qs
    return render(request, 'dockets/home.html', {'docket_list': docket_list, 'myFilter': myFilter})


def newDocket(request): #new docket form view
    submitted = False #has the form been submitted
    if request.method == "POST": #if the method is post then post the request to the DB
        form = NewDocketForm(request.POST)
        if form._is_valid(): #check for validity
            form.save() #save form to DB\
            return HttpResponseRedirect('/newDocket?submitted=True') #return a new HTTP response to pass submitte
    else:
        form = NewDocketForm
        if 'submitted' in request.GET: #if submitted is in the response set it to true, form was submitted
            submitted = True

    return render(request, 'dockets/new.html', {'form':form, 'submitted':submitted}) #render the page


