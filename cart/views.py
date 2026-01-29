from django.shortcuts import render, get_object_or_404, redirect, reverse
from  add_products.models import Products
from django.contrib.auth.decorators import login_required
from . models import Cart
from add_products.models import Products
import random
from decimal import Decimal
from . models import Cart
import stripe

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

@login_required(login_url="login")
def cart_checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect("cart")

    grand_total = sum(item.total_price() for item in cart_items)

    checkout_session = stripe.checkout.Session.create(
        mode="payment",
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": "Cart Checkout",
                    },
                    "unit_amount": int(grand_total * 100),
                },
                "quantity": 1,
            }
        ],
        success_url=request.build_absolute_uri(
            reverse("payment_success")
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse("cart")),
    )

    # 🔴 THIS LINE IS WHAT REDIRECTS TO PAYMENT
    return redirect(checkout_session.url)
