from django.shortcuts import render

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


def new(request):
    return render(request, 'dockets/new.html')


