from rest_framework.serializers import ModelSerializer
from .models import Orders, OrderProducts


class OrderSerializer(ModelSerializer):
    model = Orders
    fields = "__all__"


class OrderProductSerializer(ModelSerializer):
    model = OrderProducts
    fields = "__all__"
