from django.shortcuts import render,redirect, get_object_or_404
from  add_products.models import Products
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.models import User

# @never_cache
@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return redirect('user')
    
    if request.method == "POST":
        image = request.FILES.get('image')
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        product_types = request.POST.get('product_type')
        status = request.POST.get('status')
        vendor_name = request.POST.get('vendor_name')

        if not product_id:
            messages.error(request, "Product ID is required")
            return redirect('home:dashboard')

        if Products.objects.filter(product_id=product_id).exists():
            messages.error(request, 'The id should be unique')
            return redirect('home:dashboard')
        
        Products.objects.create(
            user = request.user,
            image=image,
            price=price,
            product_id = product_id,
            quantity = quantity,
            product_types = product_types,
            status = status,
            vendor_name = vendor_name
        )
        return redirect('home:dashboard')
        
        # messages.error(request, "Product ID should be unique")
    
    products = Products.objects.all().order_by('product_id')
    return render(request, 'dashboard.html',{'products': products})
    # return render(request, 'add-products.html')

def edit(request, id):
    e = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            e.delete()
            return redirect('home:dashboard')
        
        quantity = request.POST['quantity']
        status = request.POST['status']
        product_types = request.POST['product_type']
        vendor_name = request.POST['vendor_name']
        image = request.FILES.get('image')
        
        e.quantity=quantity
        e.status=status
        e.product_types=product_types
        e.vendor_name=vendor_name
        e.image=image

        price = request.POST.get('price')

        if price:
            e.price = price
        if 'image' in request.FILES:
            e.image = request.FILES['image']
        e.save()
        return redirect('home:dashboard')
    return render(request, 'edit.html', {'edits':e})

