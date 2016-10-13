from django.contrib import admin
from .models import *
# Register your models here.
from .models import Doctoral ,PatientDetails,Person

class DoctoralAdmin(admin.ModelAdmin):
	list_display = ["enter_government_registered_no","doctor_name", "doctor_email_id", "timestamp"]
	list_display_links = ["timestamp"]
	list_editable = ["enter_government_registered_no"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["enter_government_registered_no", "doctor_email_id"]
	class Meta:
		model = Doctoral

class PatientDetailsAdmin(admin.ModelAdmin):
	list_display = ["patient_aadhar_no", "timestamp", "diseases_or_symptoms"]
	list_display_links = ["timestamp"]
	list_editable = ["patient_aadhar_no"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["patient_aadhar_no", "diseases_or_symptoms"]
	class Meta:
		model = PatientDetails

admin.site.register(Doctoral, DoctoralAdmin)
admin.site.register(Person)
admin.site.register(PatientDetails, PatientDetailsAdmin)