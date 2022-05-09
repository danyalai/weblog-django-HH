from django.shortcuts import render
from .models import Post


def post_list_views(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})
