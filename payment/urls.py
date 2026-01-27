from django.urls import path
from . import views

urlpatterns = [
    path('payment_session/', views.payment_session, name='payment')
]
