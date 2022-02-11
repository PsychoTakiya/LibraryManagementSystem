import imp
from django.contrib import admin
from django.urls import path, include
from LMS import views

urlpatterns = [
    path('', views.index, name='home'),
    path('display', views.booksDisplay, name='booksDisplay'),
    path('updation', views.booksUpdation, name='booksUpdation'),
    path('booksDeletion', views.booksDeletion, name='booksDeletion'),


    path('custUpdation', views.custUpdation, name='custUpdation'),
    path('readersDeletion', views.readersDeletion, name='readersDeletion'),

    path('login', views.login, name='login'),



]
