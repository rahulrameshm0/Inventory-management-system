from django.urls import path
from . import views

urlpatterns = [
    path('payment_session/', views.payment, name='payment')
]
