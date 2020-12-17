from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "nothing in the cart")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HzGWeL0FWth1zIODW79XPQuZI8WfQVHIzCLItbUhgZhpOZqkV6RxEJiJbD8bRugcZH2080HYa87UsmdcKcsRuj000IUDc5XN3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
