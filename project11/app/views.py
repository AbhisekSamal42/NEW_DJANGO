from django.shortcuts import render

# Create your views here.
from app.models import*
from django.http import HttpResponse

def insert_Topic(request):
    tn=input("Enter topic name: ")
    TO=Topic.objects.get_or_create(topic_name=tn)

    if TO[1]:
        return HttpResponse("New object is created.")
    else:
        return HttpResponse("Dear user the object is already exist.")
    
def insert_Webpage(request):
    tn=input("Enter topic name: ")
    Name=input("Enter name: ")
    Url=input("Enter url: ")
    Email=input("Enter email: ")
    TO=Topic.objects.get(topic_name=tn)
    WO=Webpage.objects.get_or_create(topic_name=TO,name=Name,url=Url,email=Email)[0]

    if WO:
        return HttpResponse("Webpage is created.")
    
def insert_Accessrecord(request):
    tn=input("Enter topic name: ")
    Name=input("Enter name: ")
    Url=input("Enter url: ")
    Email=input("Enter email: ")
    Author=input("Enter author name: ")
    Date=input("Enter date: ")
    WO=Webpage.objects.get(name=Name)
    AO=Accessrecord.objects.get_or_create(name=WO,author=Author,date=Date)

    if AO:
        return HttpResponse("Webpage is created.")