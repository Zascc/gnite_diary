"""gnite_diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sleep_data/', SleepView.as_view(), name='sleep_data'),
    path('diet_data/', DietView.as_view(), name='diet_data'),
    path('sport_data/', SportView.as_view(), name='sport_data'),
    path('event_data/', EventView.as_view(), name='event_data'),
    path('test_data/', TestDataView.as_view(), name='test_data'),
    path('interest_data/', InterestView.as_view(), name='interest_data'),
    path('most_recent_data/', RecentView.as_view(), name='most_recent_data'),
    
]
