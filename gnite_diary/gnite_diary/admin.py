from django.contrib import admin

# Register your models here.
from gnite_diary.models import *

admin.site.register(SleepInfo)
admin.site.register(DietInfo)
admin.site.register(SportInfo)
admin.site.register(EventInfo)
#admin.site.register(Entry)
