from django.shortcuts import render, get_object_or_404, redirect
from  add_products.models import Products


def cart(request):
    print("SESSION BEFORE:", request.session.get('cart'))
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart':cart})

def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Products, id=product_id)

        cart = request.session.get('cart',{})

        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += 1
        else:
            cart[str(product_id)] = {
                'product_id': product.id,
                'name': product.vendor_name,
                'price': str(product.price),
                'quantity': 1,
                'image': product.image.url if product.image else ''
            }

        request.session['cart'] = cart
        request.session.modified = True
    print("SESSION AFTER:", request.session.get('cart'))
    return redirect('cart')