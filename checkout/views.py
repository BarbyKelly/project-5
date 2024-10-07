from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q6VqHG739ZsVMd8J816USb6hTlQ2qbBtzSuPVVXkKV9Zl4nA4iO8Azy4bg7co3PjARle0Jux9MfK3wB9KUWXcOb00mXMgOx74',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
