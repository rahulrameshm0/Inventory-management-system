from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('payment_session/', views.payment_session, name='payment_session'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_cancel/', views.payment_cancel, name='payment_cancel')
]