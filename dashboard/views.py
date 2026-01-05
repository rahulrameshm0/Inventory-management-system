from django.shortcuts import render,redirect
from  add_products.models import Products

def dashboard(request):
    products = Products.objects.all().order_by('product_id')
    return render(request, 'dashboard.html',{'products': products})

def edit():
    pass

def remove_item(request, id=id):
    item = Products.objects.get(id=id)
    item.delete()
    return redirect('home:dashboard')