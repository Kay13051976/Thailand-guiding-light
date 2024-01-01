from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
#     updated_on = models.DateTimeField(auto_now=True)
#     content = models.DateTimeField(auto_now=True)
#     featured_image = CloudinaryField('image', default='placeholder')
#     excerpt = models.TextField(blank=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)
#     likes = models.ManyToManyField(User, related_name='user-likes', blank=True)
# class Meta:
#     ordering = ['-created_on']