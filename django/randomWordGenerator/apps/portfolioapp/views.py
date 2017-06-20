from django.shortcuts import render, HttpResponse, redirect
import datetime
import random
from django.utils.crypto import get_random_string
from django.template import RequestContext
# the index function is called when root is visited
# def index(request):
#   print "*"*50
#   return render(request, 'portfolioapp/index.html')

def index(request):
  # context = {"somekey":get_random_string()}
  return render(request,'portfolioapp/index.html')

# def index(request):
# 	return render(request, 'portfolioapp/index.html')

def testimonials(request):
	print request.method
	return render(request, 'portfolioapp/testimonials.html')

def aboutme(request):
	print request.method
	return render(request, 'portfolioapp/aboutme.html')

def projects(request):
	print request.method
	return render(request, 'portfolioapp/projects.html')

def create(request):
	# count = 0
	if request.method == "POST":
		count = 1
		request.session['count'] += count

		# count += request.session['count']
		#  	context = {
		# "somekey":get_random_string(),
		request.session['somekey'] = get_random_string()
		# }
	return redirect("/")

	# return render(request, 'portfolioapp/index.html')


	# request.session['name'] = request.POST['first_name']
	# if request.method == "POST":
	# 	print "*"*50
	# 	print request.POST
	# 	print request.method
	# 	print "*"*50
	# 	return redirect("/")
	# else:
	# 	return redirect("/")
		# return render(request, 'portfolioapp/projects.html')
