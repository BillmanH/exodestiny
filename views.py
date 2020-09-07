from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def control(request):
    context = {}
    return render(request, 'exodest/control.html', context)
