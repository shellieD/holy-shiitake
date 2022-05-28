from django.shortcuts import render


def custom_404_error(request, exception):
    """Custom 404 Error View"""
    return render(request, '404.html')
