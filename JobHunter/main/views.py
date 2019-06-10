from django.shortcuts import render,render_to_response
from django.template import loader
# Create your views here.
def index(request):
	return render(request, 'main/main.html')

def about(request):
	return render(request, 'main/about.html')

def joinus(request):
	return render(request, 'main/joinus.html')

def jobs(request, page=1):
	content = {}

	content['page']=page
	return render(request, 'main/jobs.html', content)