from django.shortcuts import render, redirect, HttpResponse
import datetime
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'book_app/index.html')

def success(request):
  context={
  'users': User.objects.all()
  }
  return render(request, 'book_app/success.html', context)

def add_username(request):
  postData = {
  'firstname': request.POST['firstname'],
  'lastname': request.POST['lastname'],
  'email': request.POST['email'],
  'password': request.POST['password'],
  'confirm_pw': request.POST['confirm_pw'],
  'birthday': request.POST['birthday']
  }
  model_resp = User.objects.registration(postData)
  print model_resp
  if model_resp[0]==True:
    messages.add_message(request, messages.SUCCESS, 'valid')
    print model_resp[1], "Username successfully Created"
    return redirect('/success')
  else:
    messages.add_message(request, messages.ERROR, 'Usename not valid')
    print model_resp[1], "try again "
  return redirect('/')
