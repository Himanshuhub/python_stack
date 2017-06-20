from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'portfolioapp/index.html')

def ninjas(request):
	print request.method
	return render(request, 'portfolioapp/ninjas.html')

def show(request, color):
	if color == 'blue':
		image = 'leonardo.jpg'
	elif color == 'orange':
		image = 'michelangelo.jpg'
	elif color == 'red':
		image = 'raphael.jpg'
	elif color == 'purple':
		image = 'donatello.jpg'
	else:
		image = 'notapril.jpg'
		# return render(request, 'portfolioapp/notapril.html', context)
	context = {
		'image' : image
	}
	return render(request, 'portfolioapp/purple.html', context)
