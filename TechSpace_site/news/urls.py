from django.urls import path
from . import views


urlpatterns = [
    path('', views.news, name='news'),
    path('about', views.about, name='about'),
 # re_path(r'^product_detail', views.product_detail, name='product_detail')
]
