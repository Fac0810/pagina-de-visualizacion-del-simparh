from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Estacion


# Create your views here.

def index(request):
    e = Estacion.objects.all()
    print(e)
    return render(request, 'index.html')


def hello(request, username):
    
    return HttpResponse ("<h2>Hello %s</h2>" % username)

def about(request):
    return HttpResponse ("about")


    