from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tasks(request):
    return HttpResponse('<h4>Привет Tasks TechSpace<br>It`s Work!</h4>')