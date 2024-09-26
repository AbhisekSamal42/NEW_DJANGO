from django.shortcuts import render

# Create your views here.
from app.models import*
from django.http import HttpResponse

def insert_Topic(request):
    tn=input("Enter Topicname: ")
    TO=Topic.objects.get_or_create(topic_name=tn)

    if TO[1]:
        return HttpResponse("New object is created.")
    else:
        return HttpResponse("Dear user the object is already exist.")
    

def insert_Webpage(request):
    tn=input("Enter Topicname: ")
    Name=input("Enter name: ")
    Url=input("Enter url: ")

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(topic_name=TO,name=Name,url=Url)

    if WO[1]:
        return HttpResponse("New object is created.")
    else:
        return HttpResponse("Dear user the object is already exist.")
    

def insert_Accessrecord(request):
    tn=input("Enter Topicname: ")
    Name=input("Enter name: ")
    Url=input("Enter url: ")
    Author=input("Enter authorname: ")
    Date=input("Enter date: ")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(topic_name=TO,name=Name,url=Url)[0]
    AO=Accessrecord.objects.get_or_create(name=WO,author=Author,date=Date)

    if AO[1]:
        return HttpResponse("New object is created.")
    else:
        return HttpResponse("Dear user the object is already exist.")




    