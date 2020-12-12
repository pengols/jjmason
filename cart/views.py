from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ returns shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Adds items to cart """

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

    request.session['cart'] = cart
    return redirect(redirect_url)
