from django.urls import path
from . import views
urlpatterns = [
    path('', views.user, name='user'),
    path('cart/', views.cart, name='cart'),
    path('product_details/<int:id>/', views.product_details, name='product_details'),
]
