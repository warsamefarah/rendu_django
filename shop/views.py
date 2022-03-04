from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Product


def index(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('Name', '')
        desc = request.POST.get('Desc', '')
        stock = request.POST.get('Stock', 0)
        if name and desc and stock:
            if not len(list(Product.objects.filter(product_name=name))):
                product = Product(product_name=name, product_desc=desc, product_stock=stock)
                product.save()
        request.method = 'GET'

    products = list(Product.objects.all())
    if not len(products):
        product = Product(product_name='Product 1', product_desc='This is a product', product_stock=3)
        product.save()
        products.append(product)
    context = {
        'products': products,
    }

    return render(request, 'shop/index.html', context)


def detail(request, name):
    product = get_list_or_404(Product, product_name=name)
    return render(request, 'shop/detail.html', {'product': product[0]})


def remove(request, name):
    product_list = get_list_or_404(Product, product_name=name)
    product = product_list[0]
    product.product_stock = product.product_stock - 1
    if not product.product_stock:
        product.delete()
    else:
        product.save(force_update=True)
    products = list(Product.objects.all())
    context = {
        'products': products,
    }

    return HttpResponseRedirect(reverse('shop:index', args=context))
