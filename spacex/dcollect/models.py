from django.db import models
import requests
import json
from django.http import HttpResponse,JsonResponse
import dateutil.parser

class Rdata(models.Model):
    flight_number = models.IntegerField()
    rocket_name = models.CharField(max_length=270)
    mission_patch_link = models.CharField(max_length=2000, null=True,blank=True)
    date = models.CharField(max_length=270)


    def dataget():


        l=[]
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
        return l