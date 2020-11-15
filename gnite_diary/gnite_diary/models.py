from django.db import models

# Create your models here.
 
class SleepInfo(models.Model):
	usr_id = models.CharField(max_length=200)
	SleepLength = models.FloatField()
	date_added = models.DateTimeField(auto_now_add=True)
	def get_sleep_length(self):
		return self.SleepLength
	def get_usr_id(self):
		return self.usr_id

		
class DietInfo(models.Model):
	usr_id = models.CharField(max_length=200)
	calorie = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	def get_calorie(self):
		return self.calorie
	

class SportInfo(models.Model):
	usr_id = models.CharField(max_length=200)
	step_number = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	def get_step_number(self):
		return self.step_number
	

class EventInfo(models.Model):
	usr_id = models.CharField(max_length=200)
	emotion = models.CharField(max_length=10)
	catagory = models.CharField(max_length=20)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def get_emotion(self):
		return self.emotion
	def get_catagory(self):
		return self.catagory
	
class TestData(models.Model):
	name = models.CharField(max_length=20)
	cols = models.IntegerField()
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	img = models.CharField(max_length=200)

class Interest(models.Model):
	name = models.CharField(max_length=20)
	cols = models.IntegerField()
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	img = models.CharField(max_length=200)

'''class Entry(models.Model):
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'
 
	def __str__(self):
		return self.text[:50]+"..."'''
