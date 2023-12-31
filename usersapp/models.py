from django.db import models

# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

# class YourAccount(models.Model):
#     your_account_id = ShortUUIDField(length=7, max_length=25, alphabet='abcdefghijklmnopqrstuvwxyz')
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = CloudinaryField('avatar', folder='avatars', blank=True, null=True)
