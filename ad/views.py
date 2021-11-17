
from django.shortcuts import render
from .forms import ProductForm
from .services import get_product_all,all_categories
from django.core.paginator import Paginator
from .models import Product
# Create your views here.

num = 4

def details(request):
    return render(request,'ads-details.html',{})

def post_ad(request):
    forms = Product()
    # if request.POST:
    #     forms.title = request.POST.get("title")
    #     forms.category = request.POST.get("category")
    #     forms.price = request.POST.get("price")
    #     forms.decription = request.POST.get("decription")
    #     forms.phone_number = request.POST.get("phone_number")
    #     #forms.location = request.POST.get("location")
    #     forms.created_date = request.POST.get("created_date")
    #     forms.user = request.POST.get("user")
    #     forms.save()


    ctx = {
      'forms':forms,
    }

    return render(request , 'post-ads.html' ,ctx)

def categories(request):
    products = get_product_all()
    print('>>>>>>',products)
    categories_all = all_categories()
    paginator = Paginator(products, num)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    page_count = paginator.num_pages
    page_l = []

    for i in range(1, page_count):
        page_l.append(i)
    return render(request, 'ads.html', {'page_obj': page_obj,'page_l':page_l,'categories':categories_all})

def HomeCategory(request):
    products = get_product_all()
    return render(request,'index.html',{'products':products})
