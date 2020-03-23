from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path("", views.uploadhome, name='uploadhomenew'),
    path('home/result/', views.result, name='result'),
    path('home/clear/', views.clear, name='clear'),
    path('waiting/', views.waitscreen, name='waitscreen'),
]
