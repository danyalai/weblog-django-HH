from turtle import title
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User

from .models import Post
from .forms import NewPostForm


def post_list_views(request):
    posts_list = Post.objects.filter(status="pub").order_by('-datetime_modified')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_form(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
            # form = NewPostForm()
    else:
        form = NewPostForm()
    return render(request, 'blog/add_post.html', context={'form': form})


def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts_list')
    return render(request, 'blog/add_post.html', context={'form': form})

    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     user = User.objects.all()[0]
    #     Post.objects.create(title=post_title,text=post_text, author=user ,status='pub')
    #     # print(request.POST.get('title'))
    #     # print(request.POST.get('text'))
    # else:
    #     print('GET request')
    # return render(request, 'blog/add_post.html')
