from django.urls import path
from .views import blog, add_post, add_db, add_commet

urlpatterns = [
    path('blog/blog_content/', blog, name='blog'),
    path('add_post/', add_post, name='add_post'),
    path('add_post/', add_db, name ='add_blog'),
    path('blog_content/<int:id>', add_commet, name ='commet')
]



