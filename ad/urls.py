from django.urls import path, include
from .views import details, post_ad,categories,HomeCategory
urlpatterns = [
    path('', HomeCategory, name='home'),
    path('details/', details, name='details'),
    path('post/',post_ad,name = 'post_ad'),
    path('categories/',categories,name='categories')

]
