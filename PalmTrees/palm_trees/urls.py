from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('verify/<str:token>/', views.verify_email, name='verify_email'),
    path('login/', views.login, name='login'),
    path('cart/', views.cart, name='cart')
]
# This file defines the URL patterns for the Palm Trees application.