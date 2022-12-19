from django.contrib import admin
from django.urls import path, include
from .views import CartView


urlpatterns = [
    path('cart/add/<int:id>/', CartView.as_view(), name='cart-add')
]