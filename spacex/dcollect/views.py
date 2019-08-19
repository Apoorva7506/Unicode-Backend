from django.shortcuts import render
import requests
import json
from django.http import HttpResponse,JsonResponse
import dateutil.parser

def index(request):
    l = []
    r = requests.get('https://api.spacexdata.com/v3/launches')
    json_data = json.loads(r.text)
    for i in range (len(json_data)):

        dstr= json_data[i]['launch_date_utc']
        dobj= dateutil.parser.parse(dstr)
        j={'flight_number': (json_data[i]['flight_number']),
        'rocket_name': (json_data[i]['rocket']['rocket_name']),
        'missionpatch':(json_data[i]['links']['mission_patch']),
        'date': (dobj.day,dobj.month,dobj.year)
        }
        l.append(j)


    return HttpResponse(l)