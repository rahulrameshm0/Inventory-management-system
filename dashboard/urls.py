from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete/<int:id>/', views.remove_item, name='delete'),
    path('edit/<int:id>', views.edit, name='edit')
]
