from django.db import models

# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)