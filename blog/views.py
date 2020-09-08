from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def blog(request):

    all_posts = Post.newmanager.all()

    return render(request, 'blog/blog.html', {'posts': all_posts})


def post_single(request, post):
    """ Gathers the selected post that quealys the slug"""

    post = get_object_or_404(Post, slug=post, status='published')

    return render(request, 'blog/single.html', {'post': post})

