from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from profiles.models import UserProfile


def post_list(request):
    post_list = BlogPost.objects.filter(status=1).order_by('-post_created')

    context = {
        'post_list': post_list,
        
    }

    return render(request, 'blog/blog.html', context)


