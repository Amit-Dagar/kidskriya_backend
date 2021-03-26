from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from schools.models import Schools
from helper.helper import modifyPhoneNumber
import uuid


class MyAccountManager(BaseUserManager):
    def create_user(self, phone, name, password=None):
        phone = modifyPhoneNumber(phone)
        user = self.model(
            phone=phone,
            name=name
        )
        user.set_password(password)
        user.is_staff = False
        user.is_school = False
        user.is_verified = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, name):
        user = self.create_user(
            phone=phone,
            name=name,
            password=password
        )
        user.is_staff = True
        user.is_school = True
        user.is_active = True
        user.is_verified = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(
        verbose_name="email", max_length=100, unique=True, blank=True, null=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_school = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    otp = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    objects = MyAccountManager()

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'users'


class UserSchools(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.OneToOneField(Schools, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)

    class Meta:
        db_table = 'user_schools'


class Checkouts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    issued = models.DateTimeField(default=None)

    class Meta:
        db_table = "school_checkouts"