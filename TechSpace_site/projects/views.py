from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.
# def projects(request):
#    return HttpResponse('<h4>Привет Projects TechSpace<br>It`s Work!</h4>')

def projects(request):
    projects = Project.objects.order_by('-id')

    return render(request, 'projects/projects.html',
                  {'title': 'Проекты TechSpace',
                   'projects': projects,
                   })
