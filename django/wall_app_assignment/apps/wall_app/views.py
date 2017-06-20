from django.shortcuts import render
def index(request):
  return render(request, 'wall_app/index.html')

# Create your views here.
