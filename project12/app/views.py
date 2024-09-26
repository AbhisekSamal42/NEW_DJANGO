from django.shortcuts import render

# Create your views here.
from app.models import*
from django.http import HttpResponse

def insert_Country(request):
    ci=input("Enter country id: ")
    cn=input("Enter country name: ")
    CO=Country.objects.get_or_create(country_id=ci,country_name=cn)

    if CO[1]:
        return HttpResponse('Topic is Created')
    else:
        return HttpResponse('Topic is already Exists')
    
def insert_Capital(request):
    ci=input("Enter country id: ")
    cn=input("Enter country name: ")
    capid=input("Enter capital id: ")
    capname=input("Enter capital name: ")
    QLCO=Country.objects.filter(country_id=ci)

    if QLCO:
        CO=QLCO[0]
        CAPO=Capital.objects.get_or_create(country_id=CO,capital_id=capid,capital_name=capname)
        return HttpResponse('Webpage is Created')
    else:
        return HttpResponse('Dear User Given Topic is Not Avaialble')
