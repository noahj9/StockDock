from django.shortcuts import render
from .forms import NewDocketForm
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar

dockets = [
    {
        'number': '01',
        'rep': 'AR',
        'client': 'APPLE',
        'content': 'stuff here',
        'date': 'August 2, 2022'
    },
    {
        'number': '02',
        'rep': 'AR3',
        'client': 'MSFT',
        'content': 'stuff here',
        'date': 'August 3, 2022'
    }
]

def home(request):
    context = {
        'dockets': dockets
    }
    return render(request, 'dockets/home.html', context)


def newDocket(request):
    submitted = False #has the form been submitted
    if request.method == "POST": #if the method is post then post the request to the DB
        form = NewDocketForm(request.POST)
        if form._is_valid(): #check for validity
            form.save() #save form to DB\
            return HttpResponseRedirect('/newDocket?submitted=True')
    else:
        form = NewDocketForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'dockets/new.html', {'form':form, 'submitted':submitted})


