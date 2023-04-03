from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *


def insert(request):
    t_id=input('enter Topic id : ')
    T1=Topic.objects.get_or_create(topic_id=t_id)[0]
    T1.save()
    return HttpResponse('topic inserted success fully ')

def Webpages(request):
    t_id=input('enter Topic id : ')
    T1=Topic.objects.get_or_create(topic_id=t_id)[0]
    T1.save()
    tname=input('enter trainer Name : ')
    url=input('enter URL : ')
    W1=Webpage.objects.get_or_create(topic_id=T1,t_name=tname,url=url)[0]
    W1.save()
    return HttpResponse('webpage date is  inserted success fully ')

def AccessRecords(request):
     t_id=input('enter Topic id : ')
     T1=Topic.objects.get_or_create(topic_id=t_id)[0]
     T1.save()
     tname=input('enter topic name: ')
     W1=Webpage.objects.get_or_create(t_name=tname)[0]
     W1.save()
     authours=input('enter authors name:  ')
     dates=input('enter date : ')
     A1=AccessRecord.objects.get_or_create(t_name=W1,author=authours,date=dates)[0]
     A1.save()
     return HttpResponse('AccessRecords is inserted successfully ')





    



