from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('home/', views.uploadhome, name='uploadhome'),
    path('home/result', views.result, name='result'),
]
