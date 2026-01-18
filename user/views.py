from django.shortcuts import render,redirect, get_object_or_404
from add_products.models import Products
# Create your views here.
def user(request):
    return render(request, 'user-dashboard.html')

def cart(request):
    return render(request, 'cart.html')

def product_details(request, id):
    product =  get_object_or_404(id=id)
    return render(request, 'product-details.html', {'product': product})