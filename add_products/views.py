from django.shortcuts import render, redirect
from . models import Products
# Create your views here.
def add_new_products(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        quantity = request.POST.get('quantity')
        product_types = request.POST.get('product_type')
        status = request.POST.get('status')
        vendor_name = request.POST.get('name')

        Products.objects.create(
            product_id = id,
            quantity = quantity,
            product_types = product_types,
            status = status,
            vendor_name = vendor_name
        )

        return redirect('home:dashboard')
    
    return render(request, 'add-products.html')