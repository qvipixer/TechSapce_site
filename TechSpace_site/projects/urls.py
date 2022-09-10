from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    # re_path(r'^product_detail', views.product_detail, name='product_detail')
]
