from django.shortcuts import render, redirect, HttpResponse
import datetime
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'book_app/index.html')

def success(request):
  context={
  'names': User.objects.all()
  }
  return render(request, 'book_app/success.html', context)

def add_username(request):
  postData = {
  'name': request.POST['name'],
  'interest': request.POST['interest']
  }
  return redirect('/success')
