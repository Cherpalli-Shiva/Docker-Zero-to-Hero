from django.urls import HttpResponse

def home(request):
    return HttpResponse("Hello, This is the homepage!")
