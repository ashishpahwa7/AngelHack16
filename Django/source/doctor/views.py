from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import DocForm
from .models import Doctoral

# Create your views here.
def doctor_form(request):
	form = DocForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		#print form.cleaned_data.get('title')
		instance.save()


	# if request.method == 'POST':
	# 	print(request.POST.get('content'))
	# 	print(request.POST.get('title'))

	context = {
		'form' : form ,
	}
	#return HttpResponse('<h1> Hello!!</h1>')
	return render(request, 'docform.html',context)



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






