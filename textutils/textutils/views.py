# This file is created by Akanksh
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello')

def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponse('Contact')