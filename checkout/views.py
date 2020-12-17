from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "nothing in the cart")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HzGWeL0FWth1zIODW79XPQuZI8WfQVHIzCLItbUhgZhpOZqkV6RxEJiJbD8bRugcZH2080HYa87UsmdcKcsRuj000IUDc5XN3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
