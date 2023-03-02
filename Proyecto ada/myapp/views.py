from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def hello(request, username):
    
    return HttpResponse ("<h2>Hello %s</h2>" % username)

def about(request):
    return HttpResponse ("about")


    