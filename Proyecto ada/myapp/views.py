from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.

def index(request):
    return render(request, 'index.html')


def hello(request, username):
    
    return HttpResponse ("<h2>Hello %s</h2>" % username)

def about(request):
    return HttpResponse ("about")

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', { 'projects' : projects})

def tasks(request):
    #tasks = list(Task.objects.values())
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks' : tasks})
    