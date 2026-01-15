from django.urls import path
from . import views
urlpatterns = [
    path('login', views.sign_in, name='login'),
    path('signup', views.sign_up, name='signup'),
    path('logout/', views.log_out, name='logout')
]
