from django.shortcuts import render
import httplib2
import json
from django.shortcuts import redirect



# Create your views here.


def user_login(request):
	
	if request.method=='POST':
		
		username = request.POST['aadar']
		password = request.POST['password']

		URL = ('http://localhost:5000/user_login?uid=%s'%(username))
		#print URL
		h = httplib2.Http()
		response, content = h.request(URL,'POST')
		result = json.loads(content)
		#print result

		print result['data']['uid']
		print result['data']['dob']
		print username
		print password
		#return redirect('lobo.views.home_page')

		if (result['data']['uid']== username and result['data']['dob'] == password):
			print 'Success'
			return redirect('lobo.views.home_page')


	return render(request, 'lobo/user_login.html', {})



def home_page(request):

	return render(request, 'lobo/home_page.html', {'data':'This is your home page'})



