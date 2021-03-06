from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        if isinstance(quantity, int):
            product = get_object_or_404(Product, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for print_size, quantity in quantity['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'print_size': print_size,
                })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context
