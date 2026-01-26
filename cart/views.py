from django.shortcuts import render, get_object_or_404, redirect
from  add_products.models import Products
from django.contrib.auth.decorators import login_required
from . models import Cart
from add_products.models import Products
import random
from decimal import Decimal

@login_required(login_url='login')
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    grand_total = Decimal('0.00')

    for item in cart_items:
        grand_total += item.products.price * item.quantity

    gst = grand_total * Decimal('0.05')
    final_total = grand_total + round(gst)

    return render(request, 'cart.html', {'cart_items':cart_items, 'grand_total':grand_total, 'final_total':final_total})

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

def remove_cart_item(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk, user=request.user)
    cart_item.delete()
    return redirect('cart')