from django.shortcuts import render, HttpResponse
# the index function is called when root is visited
# def index(request):
#   print "*"*50
#   return render(request, 'portfolioapp/index.html')

def index(request):
	return render(request, 'portfolioapp/index.html')
def show(request):
	print request.method
	return render(request, 'portfolioapp/showusers.html')
