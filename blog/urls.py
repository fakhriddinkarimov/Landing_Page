from django.urls import path
from .views import blog

urlpatterns = [
    path('blog/blog_content/', blog, name='blog'),
]