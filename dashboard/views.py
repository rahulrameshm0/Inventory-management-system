from django.shortcuts import render,redirect, get_object_or_404
from  add_products.models import Products
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required(login_url='login')
def dashboard(request):
    products = Products.objects.all().order_by('product_id')
    return render(request, 'dashboard.html',{'products': products})

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