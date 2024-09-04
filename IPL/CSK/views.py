from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Dhoni(request):
    return HttpResponse('<h1>Dhoni is very good cricketer.</h1>')

def Raina(request):
    return render(request,'Raina.html')