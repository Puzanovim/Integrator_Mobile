from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'contact/', views.contact, name='contact'),
]
