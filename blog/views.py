from django.shortcuts import render
from .services import get_blog, get_comments


# Create your views here.

def blog(request):
    blog = get_blog()

    ctx = {
        'blogs': blog
    }
    return render(request, 'blog/blog.html', ctx)
