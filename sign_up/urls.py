from django.urls import path
from sign_up import views 

urlpatterns = [
    path('sign_up/',views.signup),
]