from django.urls import path
from .api import OrderPurchase, ReadOrders, UpdateOrder

urlpatterns = [
    path("checkout", OrderPurchase.as_view()),
    path("read", ReadOrders.as_view()),
    path("update/<str:id>", UpdateOrder.as_view()),
]
