from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_POSTAGE_THRESHOLD:
        postage = total * Decimal(settings.STANDARD_POSTAGE_PERCENTAGE / 100)
        free_postage_delta = settings.FREE_POSTAGE_THRESHOLD - total
    else:
        postage = 0
        free_postage_delta = 0

    grand_total = postage + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'postage': postage,
        'free_postage_delta': free_postage_delta,
        'free_postage_threshold': settings.FREE_POSTAGE_THRESHOLD,
        'grand_total': order_total,  
    }

    return context
