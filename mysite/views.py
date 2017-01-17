from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Riverside Nursery',
    }

    return render(request, 'mysite/index.html', context)


def test(request):
    return HttpResponse("TESTING")
