from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('webcam', views.webcam, name='webcam'),
    path('detail', views.detail, name='detail'),
    path('about', views.about, name='about'),
]
