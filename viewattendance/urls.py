from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('studentlogin/', views.student_login, name='studentlogin'),
    path('teacherlogin/', views.teacher_login, name='teacherlogin'),
    path('admin/', admin.site.urls),
    ]
