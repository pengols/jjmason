from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ returns products page and search results"""

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You need to enter something")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(publisher__icontains=query) | Q(illustrator__icontains=query) | Q(isbn__icontains=query) | Q(original_author__icontains=query)
            products = products.filter(queries)

        if request.GET:
            if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                products = products.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'search': query,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)


def single_product(request, product_id):
    """ returns detailed view for single product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/single_product.html', context)
