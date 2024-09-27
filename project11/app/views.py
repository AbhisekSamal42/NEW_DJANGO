from django.shortcuts import render

# Create your views here.
from app.models import*
from django.http import HttpResponse

def insert_Topic(request):
    tn=input("Enter topic name: ")
    TO=Topic.objects.get_or_create(topic_name=tn)

    if TO[1]:
        Topics=Topic.objects.all()
        D={'Topics':Topics}
        return render(request,'display_Topics.html',D)
        #return HttpResponse("New object is created.")
    else:
        return HttpResponse("Dear user the Topic is already exist.")
    
def insert_Webpage(request):
    tn=input("Enter topic name: ")
    Name=input("Enter name: ")
    Url=input("Enter url: ")
    Email=input("Enter email: ")
    TO=Topic.objects.get(topic_name=tn)
    WO=Webpage.objects.get_or_create(topic_name=TO,name=Name,url=Url,email=Email)[0]

    if WO:
        Webpages=Webpage.objects.all()
        D={'Webpages':Webpages}
        return render(request,'display_Webpages.html',D)
        #return HttpResponse("Webpage is created.")
    else:
        return HttpResponse("Dear user the webpage is already exist.")
    
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
        Accessrecords=Accessrecord.objects.all()
        D={'Accessrecords':Accessrecords}
        return render(request,'display_Accessrecords.html',D)
        #return HttpResponse("Webpage is created.")
    else:
        return HttpResponse("Dear user the Accessrecord is already exist.")
    

def display_Topics(request):
    Topics=Topic.objects.all()
    D={'Topics':Topics}
    return render(request,'display_Topics.html',D)

def display_Webpages(request):
    Webpages=Webpage.objects.all()
    D={'Webpages':Webpages}
    return render(request,'display_Webpages.html',D)

def display_Accessrecords(request):
    Accessrecords=Accessrecord.objects.all()
    D={'Accessrecords':Accessrecords}
    return render(request,'display_Accessrecords.html',D)