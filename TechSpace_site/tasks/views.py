from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Tasks


# Create your views here.
def tasks(request):
    tasks = Tasks.objects.order_by('status')  # сортировка в обратном порядке
    tasks_true = Tasks.objects.filter(status='True')
    tasks_false = Tasks.objects.filter(status='False')
    return render(request, 'tasks/tasks.html',
                  {'title': 'Список задач TechSpace',
                   'tasks': tasks,
                   'tasks_true': tasks_true,
                   'tasks_false': tasks_false})
