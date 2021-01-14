from django.shortcuts import render, get_object_or_404, redirect, reverse
from profiles.models import UserProfile
from django.contrib import messages

from .models import BlogPost
from .forms import BlogForm


def post_list(request):
    if request.user.is_superuser:
        post_list = BlogPost.objects.filter().order_by('-post_created')
    else:
        post_list = BlogPost.objects.filter(status=1).order_by('-post_created')

    context = {
        'post_list': post_list,
        }

    return render(request, 'blog/blog.html', context)


def add_post(request):
    """adds new blog post"""
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'new blog post added')
            return redirect(reverse('add_post'))
        else:
            messages.error(request,
                           'Post not added - check the form for errors')
    else:
        form = BlogForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_post(request, post_id):
    """edit blog post"""
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully edited blog post')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'failed to update - please check form')
    else:
        form = BlogForm(instance=post)
        messages.info(request, f'you are editing {post.post_title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def delete_post(request, post_id):
    """deletes blog post"""
    post = get_object_or_404(BlogPost, pk=post_id)
    post.delete()
    messages.success(request, f'you have deleted {post.post_title}')
    return redirect(reverse('blog'))
