from django.db import models
from schools.models import Schools, Classes
from account.models import User
from helper import helper


# Orders Model
class Orders(models.Model):
    id = models.UUIDField(
        primary_key=True, default=helper.getUniqueId(), editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    price = models.FloatField()
    status = models.IntegerField()
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
