from django.db import models
from django.core.files.storage import FileSystemStorage
from schools.models import Schools, Classes
from account.models import User
from helper import helper
import uuid
  

def filePath(instance, filename):
    return helper.os.path.join("products/%s/" % instance.id, filename)


# Products model
class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    cls = models.ForeignKey(Classes, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    banner = models.FileField(upload_to=filePath)
    price = models.FloatField()
    discount = models.IntegerField(default=0)
    stock = models.IntegerField(default=1)
    visibility = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products"


# Product Reviews
class ProductReviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product_reviews"
