from django.db.models import manager
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Orders, OrderProducts


class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProducts
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class ReadOrderSerializer(ModelSerializer):
    products = SerializerMethodField("getProducts")
    username = SerializerMethodField("getUsername")
    email = SerializerMethodField("getEmail")

    class Meta:
        model = Orders
        fields = [
            "id",
            "price",
            "payment_method",
            "address",
            "additional",
            "status",
            "created",
            "products",
            "username",
            "email",
        ]

    def getProducts(self, obj):
        queryset = OrderProducts.objects.filter(order_id=obj.id)
        return OrderProductSerializer(queryset, many=True).data

    def getUsername(self, obj):
        return obj.user.name

    def getEmail(self, obj):
        return obj.user.email