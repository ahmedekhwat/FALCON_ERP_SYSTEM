from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {'name':'Ahmed','age':20}
    return render(request, 'tasks/index.html', data)
