from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Captian(request):
    return HttpResponse('<h1>ROHIT Sharma is the great Captian.</h1>')

def Vicecaptian(request):
    return HttpResponse('<h1>JASPRIT is the best bolwer.</h1>')