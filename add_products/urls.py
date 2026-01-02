from django.urls import path
from . import views
urlpatterns = [
    path('add_products/', views.add_new_products, name='add_products')
]
