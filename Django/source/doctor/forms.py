from django import forms

from .models import Doctoral

class DocForm(forms.ModelForm):
	class Meta:
		model = Doctoral
		fields = [
			# 'title',
			# 'content'



		]