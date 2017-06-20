from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
# def index(request):
#   print "*"*50
#   return render(request, 'portfolioapp/index.html')

def index(request):
	return render(request, 'portfolioapp/index.html')

# /ninjas
def ninjas(request):
	print request.method
	return render(request, 'portfolioapp/ninjas.html')

def show(request, color):
	if color == 'blue':
		context = {
		'color' : color
		}
		return render(request, 'portfolioapp/blue.html', context)
	else:
		context = {
		'color' : color
		}
		return render(request, 'portfolioapp/blue.html', context)


def aboutme(request):
	print request.method
	return render(request, 'portfolioapp/aboutme.html')

def projects(request):
	print request.method
	return render(request, 'portfolioapp/projects.html')

def create(request):
	request.session['name'] = request.POST['first_name']

	if request.method == "POST":
		print "*"*50
		print request.POST
		print request.method
		print "*"*50
		return redirect("/")
	else:
		return redirect("/")
		# return render(request, 'portfolioapp/projects.html')
