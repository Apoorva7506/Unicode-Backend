from .models import Rdata
from django.shortcuts import render
import requests
import json
from django.http import HttpResponse,JsonResponse
import dateutil.parser

def index(request):

    
    
    y=Rdata.objects.all()
    return render(request,'index.html',{'yr':y })
    
    