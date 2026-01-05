from django.shortcuts import render, redirect
from . models import Products
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def add_new_products(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        product_types = request.POST.get('product_type')
        status = request.POST.get('status')
        vendor_name = request.POST.get('vendor_name')

        if Products.objects.filter(product_id=product_id).exists():
            messages.error(request, 'The id should be unique')
            return redirect('add_products')
        
        if Products.objects.filter(vendor_name=vendor_name).exists():
            messages.error(request, 'Vendor name should be unique')
            return redirect('add_products')
        
        try:  
            Products.objects.create(
                product_id = product_id,
                quantity = quantity,
                product_types = product_types,
                status = status,
                vendor_name = vendor_name
            )
        
        except IntegrityError:
            messages.error(request, "Product ID should be unique")
            return redirect('add_products')

        return redirect('home:dashboard')
    
    return render(request, 'add-products.html')
