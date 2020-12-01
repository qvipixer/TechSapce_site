from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Tasks


# Create your views here.
def tasks(request):
    tasks = Tasks.objects.order_by('status')  # сортировка в обратном порядке
    return render(request, 'tasks/tasks.html',
                  {'title': 'Список задач TechSpace',
                   'tasks': tasks})
