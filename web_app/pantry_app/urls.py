from django.urls import path

from . import views

#TODO add more paths 

urlpatterns = [
    path('', views.index, name='index'),
]