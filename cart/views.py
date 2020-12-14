from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """ returns shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Adds items to cart """

    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(request, f'added another {product.name} {print_size} to your bag')
            else:
                cart[item_id]['items_by_size'][print_size] = quantity
                messages.success(request, f'added {product.name} {print_size} to your bag')
        else:
            cart[item_id] = {'items_by_size': {print_size: quantity}}
            messages.success(request, f'added {product.name} {print_size} to your bag')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'added another {product.name} to your bag')
        else:
            cart[item_id] = quantity
            messages.success(request, f'added {product.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    try:
        print_size = None
        if 'print_size' in request.POST:
            print_size = request.POST['print_size']
        cart = request.session.get('cart', {})

        if print_size:
            del cart[item_id]['items_by_size'][print_size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(request, f'removed {product.name} {print_size} from your bag')
        else:
            cart.pop(item_id)
            messages.success(request, f'removed {product.name} from your bag')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'error removing item')
        return HttpResponse(status=500)
