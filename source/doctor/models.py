from django.db import models
from django.utils import timezone

# Create your models here.
class Doctoral(models.Model):
	enter_government_registered_no = models.CharField(max_length = 200,default='',null=True)  #This was primary_key=True
	doctor_name = models.CharField(max_length = 100,default='',null=True)
	doctor_email_id = models.CharField(max_length = 200,default='',null=True)
	doctor_password = models.CharField(max_length = 30,default='',null=True)
	updated =  models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.enter_government_registered_no

	def __str__(self):
		return self.enter_government_registered_no



class PatientDetails(models.Model):
	patient_aadhar_no = models.CharField(max_length = 200,default='',null=True) 
	diseases_or_symptoms = models.CharField(max_length = 200,default='',null=True)
	symptoms_description = models.TextField()
	prescibed_medicines = models.CharField(max_length = 200,default='',null=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	def __unicode__(self):
		return self.patient_aadhar_no

	def __str__(self):
		return self.patient_aadhar_no
