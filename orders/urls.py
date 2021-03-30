from django.urls import path
from .api import OrderPurchase

urlpatterns = [
    path("checkout", OrderPurchase.as_view()),
]
