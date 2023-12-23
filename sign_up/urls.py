from django.shortcuts import render
from sign_up import views 

urlpatterns = [
    path('index',views.index),
]