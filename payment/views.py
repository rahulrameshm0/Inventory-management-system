from django.shortcuts import render, redirect, reverse
import stripe
from django.conf import settings
from decimal import Decimal
from . models import UserPayment
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def payment_session(request):
    product_id = 'prod_TsL7Q2BfZIKnjb'
    product = stripe.Product.retrieve(product_id)
    prices = stripe.Price.list(product=product_id)
    price = prices.data[0]
    product_price = price.unit_amount/100.0

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f'{settings.BASE_URL}{reverse('login')}?next={request.get_full_path()}')
        price_id = request.POST.get('price_id')
        quantity = int(request.POST.get('quantity'))
        checkout_sessoin = stripe.checkout.Session.create(
            line_items=[
               {
                'price':price_id,
                'quantity':quantity
                },
            ],
            payment_method_types = ['card'],
            mode = 'payment',
            customer_creation= 'always',
            success_url = request.build_absolute_uri(reverse("payment_success")) + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url = request.build_absolute_uri(reverse("payment_cancel"))
        )
        return redirect(checkout_sessoin.url)
    return render(request, 'payment.html', {'product':product, 'product_price':product_price})

def payment_success(request):
    checkout_session_id = request.GET.get('session_id', None)

    if checkout_session_id:
        session = stripe.checkout.Session.retrieve(checkout_session_id)
        customer_id = session.customer 
        customer = stripe.Customer.retrieve(customer_id)
        line_item = stripe.checkout.Session.list_line_items(checkout_session_id).data[0]
        UserPayment.objects.create(
            user = request.user,
            stripe_customer_id = customer_id,
            stripe_checkout_id = checkout_session_id,
            stripe_product_id = line_item.price.product,
            quantity = line_item.quantity, 
            price = line_item.price.unit_amount/100.0,
            currency = line_item.price.currency,
            has_paid = True 
        )


    return render(request, 'payment_successful.html', {'customer':customer})

def payment_cancel(request):
    return render(request, 'payment_cancel.html')
