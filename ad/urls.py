from django.urls import path, include
from .views import home,details
urlpatterns = [
    path('', home, name='home'),
    path('details/', details, name='details')
]
