from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from news.models import Article
from projects.models import Project


# def index(request):
#    return HttpResponse('<h4>Привет TechSpace<br>It`s Work!</h4>')


def index(request):
    articles = Article.objects.order_by("-id")[
               :3
               ]  # сортировка в обратном порядке 3 последние новсости
    projects = Project.objects.order_by("-id")[:2]
    return render(
        request,
        "home/index.html",
        {
            "title": "Главная страница TechSpace",
            "articles": articles,
            "projects": projects,
        },
    )


def webcam(request):
    return render(request, "home/webcam.html", {"title": "Online камера TechSpace"})


def detail(request):
    project_detail = Project.objects.all()
    project = request.GET.get("project")  # GET переменная

    return render(
        request,
        "home/detail.html",
        {
            "title": "Страница с полным описанием проекта",
            "project_detail": project_detail,
            "project": project,
        },
    )


def about(request):
    return render(request, "home/about.html", {"title": "Про TechSpace"})
