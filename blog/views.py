from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def post_list_views(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    print('ID IN URL', pk)
    return HttpResponse(f'Id:{pk}')
