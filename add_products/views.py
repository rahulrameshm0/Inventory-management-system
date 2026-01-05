from django.shortcuts import render, redirect
from . models import Products
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def add_new_products(request):
    if request.method == 'POST':
        product_id = request.POST.get('id')
        quantity = request.POST.get('quantity')
        product_types = request.POST.get('product_type')
        status = request.POST.get('status')
        vendor_name = request.POST.get('name')

        if Products.objects.filter(product_id=product_id).exists():
            messages.error(request, 'The id should be unique')
            return redirect('add_products')
        if Products.objects.filter(vendor_name=vendor_name).exists():
            messages.error(request, 'Vendor name should be unique')
            return redirect('add_products')
        
        Products.objects.create(
            product_id = id,
            quantity = quantity,
            product_types = product_types,
            status = status,
            vendor_name = vendor_name
        )

        return redirect('home:dashboard')
    
    return render(request, 'add-products.html')


def remove_item(request, id=id):
    item = Products.objects.get(id=id)
    item.delete()
    return redirect('home:dashboard')