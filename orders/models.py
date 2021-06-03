from django.db import models
from schools.models import Schools, Classes
from account.models import User
from helper import helper
import uuid

# Orders Model
class Orders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, null=True, blank=True)
    student_class = models.ForeignKey(
        Classes, on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.FloatField()
    payment_method = models.IntegerField(default=1)
    # 1=> COD
    # 2=>razorpay
    # payment_id = models.CharField(max_length=40, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    additional = models.TextField(null=True, blank=True)
    status = models.IntegerField()
    # 1 -> In Progress
    # 2 -> Out For Delivery
    # 3 -> Delivered
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "orders"


# order Products
class OrderProducts(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    discount = models.IntegerField()
    banner = models.CharField(max_length=800)

    class Meta:
        db_table = "order_products"
