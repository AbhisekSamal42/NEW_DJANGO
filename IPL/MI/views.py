from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Rohit(request):
    return HttpResponse('<h1>Ro super hit sharma.</h1>')

def Bhoomra(request):
    return render(request,'Bhoomra.html')