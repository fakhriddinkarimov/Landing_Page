from django.urls import path, include
from .views import home,details, post_ad,categories
urlpatterns = [
    path('', home, name='home'),
    path('details/', details, name='details'),
    path('post/',post_ad,name = 'post_ad'),
    path('categories/',categories,name='categories')
]
