from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def puri(request):
    return HttpResponse('Welcome to PURI')