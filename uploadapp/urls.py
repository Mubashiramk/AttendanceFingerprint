from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path("", views.uploadhome, name='uploadhomenew'),
    path('home/', views.uploadhome, name='uploadhome'),
    path('home/result/', views.result, name='result'),
    path('home/clear/', views.clear, name='clear'),
    path('home/test/', views.testdevice, name='testdevice'),
]
