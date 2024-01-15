from django.shortcuts import redirect

def password_protected_view(func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('authenticated'):
            return func(request, *args, **kwargs)
        return redirect('password_entry')  # Redirect to the password entry view

    return wrapper
