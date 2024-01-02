from django.urls import path
from home import views

urlpatterns=[
    path('home',views.home),
    # path('login',views.login),
    # path('logout',views.logout)
]