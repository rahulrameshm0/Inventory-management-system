from django.shortcuts import render,redirect, get_object_or_404
from add_products.models import Products
from django.core.paginator import Paginator

def user(request):
    products = Products.objects.all()
    return render(request, 'user-dashboard.html', {'products': products})

def cart(request):
    return render(request, 'cart.html')

def product_details(request, id):
    product =  get_object_or_404(id=id)
    return render(request, 'product-details.html')

def product_list(request):
    pass