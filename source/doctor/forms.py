from django import forms

from .models import Doctoral, PatientDetails

class DocForm(forms.ModelForm):
	class Meta:
		model = Doctoral
		fields = [
			'enter_government_registered_no',
			'doctor_name',
			'doctor_email_id',
			'doctor_password'



		]


class PatientForm(forms.ModelForm):
	class Meta:
		model = PatientDetails
		fields = [
			'patient_aadhar_no',
			'diseases_or_symptoms',
			'symptoms_description',
			'prescibed_medicines'



		]