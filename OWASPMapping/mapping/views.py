from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def layout(request):
    # return HttpResponse('Hello')
    return render(request, 'mapping/layout.html')


def list(request):
    # return HttpResponse('Hello')
    return render(request, 'mapping/list.html')


def add(request):
    # return HttpResponse('Hello')
    return render(request, 'mapping/add.html')
