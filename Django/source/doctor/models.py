from django.db import models
from django.utils import timezone

# Create your models here.
class Doctoral(models.Model):
	Enter_Government_Registered_No = models.CharField(max_length = 200,primary_key=True)
	Doctor_Name = models.CharField(max_length = 100)
	Doctor_Email_id = models.CharField(max_length = 50)
	Doctor_Password = models.CharField(max_length = 30)
	updated =  models.DateTimeField(default=timezone.now)
	timestamp = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.Enter_Government_Registered_No

	def __str__(self):
		return self.Enter_Government_Registered_No
