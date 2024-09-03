from django.shortcuts import render

# Create your views here.

def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """
    
    products = Products.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'home/index.html')