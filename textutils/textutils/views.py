# This file is created by Akanksh
from django.http import HttpResponse

def index(request):
    return HttpResponse('Home')

def removepunc(request):
    return HttpResponse('remove puncuation')

def capfirst(request):
    return HttpResponse('capitalize first letter')

def newlineremover(request):
    return HttpResponse('New line remover')

def spaceremover(request):
    return HttpResponse('Space remover')

def charcount(request):
    return HttpResponse('Character counter')
