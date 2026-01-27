from django.shortcuts import render
import stripe
from django.conf import settings
from decimal import Decimal


def payment_session(request):
    return render(request, 'payment.html')