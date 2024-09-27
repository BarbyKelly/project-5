from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_cart(request):
    """
    A view that renders the cart contents page
    """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """
    Add a quantity of the selected product to the shopping cart
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
    else:
        cart[item_id] = quantity
    
    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the quantity of the selected items to the specified amount
    """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            del cart[item_id]
            if not cart[item_id]:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Remove the item from the cart
    """

    try:
        cart = request.session.get('cart', {})

        if quantity:
            del cart[item_id]
            if not cart[item_id]:
                cart.pop(item_id)
        else:
            cart.pop(item_id)
        
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)