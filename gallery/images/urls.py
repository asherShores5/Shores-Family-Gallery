from django.urls import path
from .views import image_list

urlpatterns = [
    path('', image_list, name='templates/image_list'),
]
