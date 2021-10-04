from django.shortcuts import render



def multi_image(request):
    ctx = {

    }
    return render(request, 'post_ads/post_ads.html', ctx)
