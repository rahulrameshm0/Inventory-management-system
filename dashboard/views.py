from django.shortcuts import render,redirect, get_object_or_404
from  add_products.models import Products
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
import dashboard

@never_cache
@login_required(login_url='login')
def dashboard(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        product_types = request.POST.get('product_type')
        status = request.POST.get('status')
        vendor_name = request.POST.get('vendor_name')
        if Products.objects.filter(product_id=product_id).exists():
            messages.error(request, 'The id should be unique')
            return redirect('home:dashboard')
        
        try:  
            Products.objects.create(
                user = request.user,
                product_id = product_id,
                quantity = quantity,
                product_types = product_types,
                status = status,
                vendor_name = vendor_name
            )
        
        except IntegrityError:
            messages.error(request, "Product ID should be unique")
            return redirect('home:dashboard')

        return redirect('home:dashboard')
    
    products = Products.objects.filter(user=request.user).order_by('product_id')
    return render(request, 'dashboard.html',{'products': products})
    # return render(request, 'add-products.html')

def edit(request, id):
    e = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        quantity = request.POST['quantity']
        status = request.POST['status']
        product_types=request.POST['product_type']
        vendor_name=request.POST['vendor_name']
        e.quantity=quantity
        e.status=status
        e.product_types=product_types
        e.vendor_name=vendor_name
        e.save()
        return redirect('home:dashboard')
    return render(request, 'edit.html', {'edits':e})

def remove_item(request, id=id):
    item = Products.objects.get(id=id)
    item.delete()
    return redirect('home:dashboard')