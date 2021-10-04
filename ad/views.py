from django.shortcuts import render
from .forms import ProductForm

# Create your views here.


def home(request):
    return render(request,'index.html',{})

def details(request):
    return render(request,'ads-details.html',{})

def post_ad(request):
    forms = ProductForm()
    ctx = {
      'forms':forms
    }

    return render(request , 'post-ads.html' , ctx)


