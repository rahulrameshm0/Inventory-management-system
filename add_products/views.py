from django.shortcuts import render

# Create your views here.
def add_new_products(request):
    return render(request, 'add-products.html')