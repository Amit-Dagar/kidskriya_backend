from django.db import models
import uuid


class Schools(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, default="Haryana")
    pin = models.IntegerField()
    phone = models.CharField(max_length=13, unique=True)
    address = models.TextField()
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'schools'


class Classes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'classes'
