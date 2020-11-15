from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.db import Error, IntegrityError
from django.db.transaction import atomic
from .models import *
class SleepView(View):
    def get(self, request, *args, **kwargs):
        sleep_data = list(SleepInfo.objects.values())
        return JsonResponse(sleep_data, safe=False)
class DietView(View):
    def get(self, request, *args, **kwargs):
        diet_data = list(DietInfo.objects.values())
        return JsonResponse(diet_data, safe=False)
class SportView(View):
    def get(self, request, *args, **kwargs):
        sport_data = list(SportInfo.objects.values())
        return JsonResponse(sport_data, safe=False)
        
class EventView(View):
    def get(self, request, *args, **kwargs):
        event_data = list(EventInfo.objects.values())
        return JsonResponse(event_data, safe=False)
        

