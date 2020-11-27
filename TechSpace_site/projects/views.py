from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def projects(request):
    return HttpResponse('<h4>Привет Projects TechSpace<br>It`s Work!</h4>')