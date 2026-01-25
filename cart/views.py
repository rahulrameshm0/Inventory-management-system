from django.shortcuts import render, get_object_or_404, redirect
from  add_products.models import Products


def cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart':cart})

def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    cart = request.session.get('cart',{})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.vendor_name,
            'price': str(product.price),
            'quantity': 1
        }

    request.session['cart'] = cart
    return redirect('cart')