from django.urls import path
from .api import OrderPurchase, ReadOrders

urlpatterns = [
    path("checkout", OrderPurchase.as_view()),
    path("read", ReadOrders.as_view()),
]
