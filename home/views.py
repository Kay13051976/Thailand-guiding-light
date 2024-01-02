from django.shortcuts import render
from django.views import generic
from home.models import Post

# Create your views here.
class PostList(generic.ListViews):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6