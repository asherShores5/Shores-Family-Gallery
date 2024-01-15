from django.urls import path
from .views import image_list
from . import views

urlpatterns = [
    path('password/', views.password_entry, name='password_entry'),
    path('', image_list, name='image_list'),
]

