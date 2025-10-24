# Base from Boutique Ado. Edited with ChatGPT to reduce how many products load, to improve LS score
from django.shortcuts import render
from products.models import Product


def index(request):
    """
    A view to return the index.html page
    Only show first 4 products for improved performance
    """
    products = Product.objects.all()[:4]
    return render(request, 'home/index.html', {'products': products})
