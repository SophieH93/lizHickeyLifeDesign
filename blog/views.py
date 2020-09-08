from django.shortcuts import render
from .models import Post

# Create your views here.


def blog(request):

    all_posts = Post.newmanager.all()

    return render(request, 'blog/blog.html', {'posts': all_posts})
