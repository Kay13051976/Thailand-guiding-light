from django.urls import path
from social_media_project import views 

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('about',views.signup),
]