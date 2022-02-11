import imp
from django.contrib import admin
from django.urls import path, include
from LMS import views

urlpatterns = [
    path('', views.index, name='home'),
    path('display', views.booksDisplay, name='booksDisplay'),
    path('updation', views.booksUpdation, name='booksUpdation'),
    path('custUpdation', views.custUpdation, name='custUpdation'),


]
