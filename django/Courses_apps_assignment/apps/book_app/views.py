from django.shortcuts import render, redirect, HttpResponse
import datetime
from .models import Course
# Create your views here.
def index(request):
  context={
  'courses': Course.objects.all()
  }
  return render(request, 'book_app/index.html', context)

def add_course(request):
  if request.method=='POST':
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
  return redirect('/')

def delete(request,id):
  context={
  'course': Course.objects.get(id=id)
  }
  return render(request, 'book_app/delete.html', context)

def delete_course(request, id):
  if request.method=='POST':
    Course.objects.filter(id=id).delete()
  else:
    return redirect('/')  
  return redirect('/')
