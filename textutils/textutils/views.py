# This file is created by Akanksh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def removepunc(request):
    print(request.GET.get('text','default content'))
    return HttpResponse('remove puncuation')

def capfirst(request):
    return HttpResponse('capitalize first letter')

def newlineremover(request):
    return HttpResponse('New line remover')

def spaceremover(request):
    return HttpResponse('Space remover')

def charcount(request):
    return HttpResponse('Character counter')
