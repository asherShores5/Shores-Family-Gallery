from django.shortcuts import render, redirect
from .models import Image
from django.conf import settings
from django.contrib import messages
from .decorators import password_protected_view
from django.urls import reverse

@password_protected_view
def image_list(request):
    images = Image.objects.all()
    return render(request, 'images/image_list.html', {'images': images})

def password_entry(request):
    if request.method == 'POST':
        entered_password = request.POST.get('password')
        if entered_password == settings.SITE_PASSWORD:
            request.session['authenticated'] = True
            return redirect(reverse('image_list'))
        else:
            messages.error(request, 'Incorrect password')

    return render(request, 'images/password_entry.html')
