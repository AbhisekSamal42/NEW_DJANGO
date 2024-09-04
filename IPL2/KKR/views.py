from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Captian(request):
    return HttpResponse('<h1>GAMVIR is a good batsman.</h1>')

def Vicecaptian(request):
    return HttpResponse('<h1>SHREYAS is a good player.</h1>')