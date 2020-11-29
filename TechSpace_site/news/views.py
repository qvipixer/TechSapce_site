from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def news(request):
    return HttpResponse('<h4>Привет News TechSpace<br>It`s Work!</h4>')

def about(request):
    return HttpResponse('<h4>Привет about TechSpace<br>It`s Work!</h4>')