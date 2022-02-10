import imp
from django.contrib import admin
from django.urls import path, include
from LMS import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('display', views.booksDisplay, name='booksDisplay'),
]
