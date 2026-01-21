from django.urls import path
from . import views
urlpatterns = [
    path('', views.user, name='user'),
    path('logout/', views.sign_out, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('product_details', views.product_details, name='product_details'),
]
