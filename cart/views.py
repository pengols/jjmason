from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """ returns shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Adds items to cart """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    print_size = None
    if 'print_size' in request.POST:
        print_size = request.POST['print_size']

    if print_size:
        if item_id in list(cart.keys()):
            if print_size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][print_size] += quantity
            else:
                cart[item_id]['items_by_size'][print_size] = quantity
        else:
            cart[item_id] = {'items_by_size': {print_size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
            messages.success(request, f'added {product.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        print_size = None
        if 'print_size' in request.POST:
            print_size = request.POST['print_size']
        cart = request.session.get('cart', {})

        if print_size:
            del cart[item_id]['items_by_size'][print_size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
