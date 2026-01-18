from django.shortcuts import render

# Create your views here.
def user(request):
    return render(request, 'user-dashboard.html')

def cart(request):
    return render(request, 'cart.html')

def product_details(request):
    return render(request, 'product-details.html')