from django.urls import path
from .views import multi_image

urlpatterns = [
    path('',multi_image,name='multi_image')
]