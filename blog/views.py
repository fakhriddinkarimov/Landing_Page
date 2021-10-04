from django.shortcuts import render
from .services import get_blog, get_comments,get_comments, info_blog, get_category, last_commet
from .forms import BlogModelForm,BlogForm
from .models import Blog
# Create your views here.

def blog(request):
    blog = get_blog()
    categorys = get_category()
    last_commets = last_commet()
    ctx = {
        'blogs': blog,
        'categorys': categorys,
        'last_commets':last_commets
    }
    return render(request, 'blog/blog.html', ctx)


def add_post(request):
    form = BlogModelForm()
    contex ={
        'form':form
    }
    return  render(request, 'blog/post.html', contex)


def add_db(request):
    if request.POST:
        form = BlogForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print('>>>>>>')
            des = form.cleaned_data['description']
            slug = form.cleaned_data['slug']
            created_date = form.cleaned_data['created_date']
            img = form.cleaned_data['image']
            category = form.cleaned_data['category']
            db = Blog(name=name, description=des, image=img, slug=slug, created_date=created_date, category=category)
            db.save()
        else:
            print("didn't save !!!")
    return render(request, 'blog/post.html',{})

def add_commet(request,id):
    blog =info_blog(id)
    comments = get_comments(id)
    contex = {
        'blog': blog,
        'comments':comments
    }
    return render(request, 'blog/single-post.html', contex)


