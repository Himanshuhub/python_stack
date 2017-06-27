from django.shortcuts import render, redirect, HttpResponse
from .models import User, Comment
# from IPython import embed
import datetime
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'belt_app/index.html')

def books(request):
  return render(request, 'belt_app/books.html')

def book(request, bookid):
  return render(request, 'belt_app/book.html')

def user(request, userid):
  return render(request, 'belt_app/user.html')

def add(request):
  return render(request, 'belt_app/add.html')

def users(request):
  return render(request, 'belt_app/users.html')

def register(request):
  if request.method == "POST":
    validation = User.objects.regVal(request.POST)
    if validation[0]:
      request.session['current_user']=validation[1].first_name
      request.session['user_id']=validation[1].id
      return redirect("/books")
    else:
      for error in validation[1]:
        messages.error(request, error)
      return redirect('/')
  return redirect('/')

def login(request):
  if request.method == "POST":
    validation = User.objects.logVal(request.POST)

    if validation[0]:
      request.session['current_user']=validation[1].first_name
      request.session['user_id']=validation[1].id
      messages.add_message(request, messages.SUCCESS, 'valid')
      return redirect("/books")
    else:
      # for error in validation[1]:
      #   messages.error(request, error)
      messages.error(request, "Email or password invalid")
      return redirect('/')

  return redirect('/books')

def logout(request):
    request.session.clear()
    return redirect('/')


def addBook(request):
  if request.method == "POST":
    pass
  return redirect('/add')

def reviewBook(request):
  if request.method == "POST":
    pass

  return redirect('/books')

def reviewUser(request):
  if request.method == "POST":
    pass

  return redirect('/books')

def logout(request):
  if request.method == "POST":
    pass

  return redirect('/')
