from django.db import models

# Create your models here.
class Doctoral(models.Model):
	Enter_Government_Registered_No = models.CharField(max_length=20,default=None,null=False,blank=False,primary_key=True)
	Doctor_Name = models.CharField(max_length=30,default=None,null=False,blank=False)
	Doctor_Email_id = models.CharField(max_length=30,default=None,null=False,blank=False)
	Doctor_Password = models.CharField(max_length=30, default=None)
	updated =  models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.Enter_Government_Registered_No

	def __str__(self):
		return self.Enter_Government_Registered_No