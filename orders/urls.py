from django.urls import path
from .api import OrderPurchase, ReadOrder

urlpatterns = [
    path("checkout", OrderPurchase.as_view()),
    path("read", ReadOrder.as_view())
]
