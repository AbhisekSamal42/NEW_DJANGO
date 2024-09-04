from django.shortcuts import render

# Create your views here.
def jay(request):
    return render(request,'jay.html')


def lorem(request):
    return render(request,'lorem.html')