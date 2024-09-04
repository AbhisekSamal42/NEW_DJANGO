from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Captian(request):
    return HttpResponse('<h1>MSD is the best wck in the world.</h1>')

def Vicecaptian(request):
    return HttpResponse('<h1>SURESH Rina is call MR ipl.</h1>')