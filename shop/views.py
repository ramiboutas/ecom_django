from django.shortcuts import render
from shop.models import Product


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)
