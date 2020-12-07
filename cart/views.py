from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """ returns shopping cart """
    
    return render(request, 'cart/cart.html')
