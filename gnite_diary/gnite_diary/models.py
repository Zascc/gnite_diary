from django.db import models

# Create your models here.
 
class SleepInfo(models.Model):
	usr_id = models.CharField(max_length=200)
	SleepLength = models.FloatField()
	date_added = models.DateTimeField(auto_now_add=True)


		
class DietInfo(models.Model):
	usr_id = models.CharField(max_length=200)
	calorie = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)
	

class SportInfo(models.Model):
	usr_id = models.CharField(max_length=200)
	step_number = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)
	

class EventInfo(models.Model):
	usr_id = models.CharField(max_length=200)
	emotion = models.CharField(max_length=10)
	catagory = models.CharField(max_length=20)
	date_added = models.DateTimeField(auto_now_add=True)
	


'''class Entry(models.Model):
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'
 
	def __str__(self):
		return self.text[:50]+"..."'''
