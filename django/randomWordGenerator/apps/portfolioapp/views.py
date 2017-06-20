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
  if 'counter' not in request.session:
	  request.session['counter'] = 1
  return render(request,'portfolioapp/index.html')

def create(request):
	# counter = 1
	if request.method == "POST":
		request.session['counter'] += 1
		request.session['somekey'] = get_random_string()
	return redirect("/")
