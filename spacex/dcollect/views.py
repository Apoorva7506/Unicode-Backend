from .models import Rdata
from django.shortcuts import render
import requests
import json
from django.http import HttpResponse,JsonResponse
import dateutil.parser

def index(request):
    
    t=Rdata.dataget()
    for i in t:

    
        p=Rdata(flight_number=i['flight_number'],rocket_name=i['rocket_name'],mission_patch_link=i['missionpatch'],date=i['date'])
        p.save()
     
    y=Rdata.objects.all()

    return render(request,'index.html',{'yr':y })
    
    