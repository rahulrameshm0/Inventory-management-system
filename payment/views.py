from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from add_products.models import Products
import stripe
from django.contrib.auth.decorators import login_required
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required(login_url='login')
def payment_session(request,product_id):
    product = Products.objects.get(id=product_id)
    # POST → create Stripe checkout
    if request.method == "POST":
        checkout_session = stripe.checkout.Session.create(
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": product.vendor_name,
                        },
                        "unit_amount": int(product.price * 100),
                    },
                    "quantity": 1,
                }
            ],
            success_url=request.build_absolute_uri(
                reverse("payment_success")
            )
            + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.build_absolute_uri(reverse("payment_cancel")),
        )

        return redirect(checkout_session.url)
    
    return render(request, "payment.html", {"product": product,"product_price": product.price})

def payment_success(request):
    return render(request, "payment_successful.html")


def payment_cancel(request):
    return render(request, "payment_cancel.html")