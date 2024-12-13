from django.contrib import admin
from django.urls import path 
from main import views 

urlpatterns = [
    path('login', views.login, name="login"),
    path('register',views.register, name="register"),
    path('home', views.home_view, name="home"),
]