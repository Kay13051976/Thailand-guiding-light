from django.shortcuts import render
from django.views import generic
from .models import Post
from django.template.response import TemplateResponse

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 6

# def home(request):
#     home.object.filter()
#     return render(request, "home.html")

# def layout(request):
#     return render(request, "layout.html")