from django.shortcuts import render
from .models import Image

def image_list(request):
    images = Image.objects.all()
    return render(request, 'images/image_list.html', {'images': images})
