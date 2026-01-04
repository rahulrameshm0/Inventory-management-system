from django.shortcuts import render
from  add_products.models import Products

def dashboard(request):
    products = Products.objects.all()
    return render(request, 'dashboard.html',{'products': products})