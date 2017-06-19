# Controller
from django.shortcuts import render, HttpResponse
# the index function is called when root is visited
def index(request):
    # response = "Hello, I am your first request!"
    # return HttpResponse(response)

    print ("*" * 50)
    return render(request, "first_app/index.html")
