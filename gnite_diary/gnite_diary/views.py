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
class TestDataView(View):
    def get(self, request, *args, **kwargs):
        test_data = list(TestData.objects.values())
        return JsonResponse(test_data, safe=False)
        
class InterestView(View):
    def get(self, request, *args, **kwargs):
        interest_data = list(Interest.objects.values())
        return JsonResponse(interest_data, safe=False)
        
class RecentView(View):
	def get(self, request, *args, **kwargs):
		most_recent_data = {}
		most_recent_data['UserID'] = SleepInfo.objects.all()[len(SleepInfo.objects.values()) - 1].get_usr_id()
		most_recent_data['SleepLength'] = SleepInfo.objects.all()[len(SleepInfo.objects.values()) - 1].get_sleep_length()
		most_recent_data['Calorie'] = DietInfo.objects.all()[len(DietInfo.objects.values()) - 1].get_calorie()
		most_recent_data['StepNumber'] = SportInfo.objects.all()[len(SportInfo.objects.values()) - 1].get_step_number()
		most_recent_data['Emotion'] = EventInfo.objects.all()[len(EventInfo.objects.values()) - 1].get_emotion()
		most_recent_data['Catagory'] = EventInfo.objects.all()[len(EventInfo.objects.values()) - 1].get_catagory()
		
		return JsonResponse(most_recent_data, safe=False)    

