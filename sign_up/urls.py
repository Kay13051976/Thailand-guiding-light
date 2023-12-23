from django.shortcuts import render
from django.urls import path
from sign_up import views 

urlpatterns = [
    path('',views.index),
]