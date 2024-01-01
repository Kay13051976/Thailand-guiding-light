from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    connector = models.ForeignKey(User, on_delete=models.CASCADE, related_name="home_page_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    heart = models.ManyToManyField(User, related_name='home_page_hearts', blank=True)
    
    
    class Meta:
    ordering = ['-created_on']
    
    def __str__(self):
    return self.title

    def number_of_hearts(self):
    return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete-models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    created_on = model.DateTimeField(auto_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = [created_on]
        
    def __str__(self):
        return f"Comment {self.body} by {self.name}"