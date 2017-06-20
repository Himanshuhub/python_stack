from django.shortcuts import render, redirect

from .models import Book
# Create your views here.
def index(request):
  return render(request, 'book_app/index.html')
