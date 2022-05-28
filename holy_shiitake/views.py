from django.shortcuts import render


def custom_404_error(request, exception):
    """Custom 404 Error View"""
    return render(request, '404.html')


def custom_500_error(request, exception):
    """Custom 500 Error View"""
    return render(request, '500.html')
