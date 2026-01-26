from django.shortcuts import render, get_object_or_404, redirect
from  add_products.models import Products
from django.contrib.auth.decorators import login_required
from . models import Cart

@login_required(login_url='login')
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items':cart_items})

@login_required(login_url='login')
def add_to_cart(request, product_id):
    products = get_object_or_404(Products, id=product_id)
    if request.method == "POST":

        cart_items, created = Cart.objects.get_or_create(
            user = request.user,
            products=products
        )

        if not created:
            cart_items.quantity += 1
            cart_items.save()

    return redirect('cart')