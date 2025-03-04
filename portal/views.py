from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html') # Falcon Website Home Page

def about(request):
    return HttpResponse("Hello, This is the about falcon page.") # Falcon About Page

def home(request):
    return HttpResponse("Hello, This is the home falcon page (Portal).")

