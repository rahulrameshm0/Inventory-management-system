from django.shortcuts import render,redirect, get_object_or_404
from add_products.models import Products
from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.contrib.auth import login, logout

def user(request):
    products = Products.objects.all()
    
    page_number = request.GET.get('page')
    pagintor = Paginator(products, 6)
    page_obj = pagintor.get_page(page_number)

    return render(request, 'user-dashboard.html', {'page_obj':page_obj})

def cart(request):
    return render(request, 'cart.html')

def product_details(request, id):
    product =  get_object_or_404(id=id)
    return render(request, 'product-details.html')

def product_list(request):
    pass

def sign_out(request):
    logout(request)
    return redirect('')