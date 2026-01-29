from django.urls import path
from . import views
from payment.views import payment_session
urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/<int:pk>/', views.remove_cart_item, name='remove_cart'),
    path('cart_checkout/', views.cart_checkout, name='cart_checkout'),
]
