from home import views
from django.urls import path

urlpatterns=[
    path('', views.PostList.as_view(), name='home')
    # path('home',views.home),
    # path('layout',views.layout),
    
    # path('login',views.login),
    # path('logout',views.logout)
]