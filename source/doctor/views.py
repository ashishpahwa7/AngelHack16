from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DocForm, PatientForm
from .models import Doctoral, PatientDetails
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login



# Create your views here.
def doctor_form(request):
	form = DocForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print(form.cleaned_data.get('enter_government_registered_no'))
		instance.save()


	# if request.method == 'POST':
	# 	print(request.POST.get('content'))
	# 	print(request.POST.get('title'))

	context = {
		#'form' : form ,
	}
	#return HttpResponse('<h1> Hello!!</h1>')
	return render(request, 'docform.html',context)




def patient_checkup(request):
	form = PatientForm(request.POST or None)
	#print (form)
	if form.is_valid(): 
		#print (form)                     # THIS PART CREATING THIS ERROR:
		instance=form.save(commit=False)       #NOT NULL constraint failed: doctor_patientdetails.diseases_or_symptoms
		print(form.cleaned_data.get('patient_aadhar_no'))
		instance.save()

	return render(request,'pat_check.html',{})





def doc_data(request):
	queryset = Doctoral.objects.all()
	context = {
		'object_list': queryset,
		'title':'List'

	}
	return render(request,'docdata.html',context)



def doc_login(request):

	return render(request,'doclogin.html',{})




def pat_check(request):

	return render(request,'pat_check.html',{})






