from django.shortcuts import render
import stripe
from django.conf import settings
from decimal import Decimal

stripe.api_key = settings.STRIPE_API_KEY
DOMAIN = settings.DOMAIN

def payment_session(request):
    pass