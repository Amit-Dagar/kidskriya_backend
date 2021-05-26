from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    Serializer,
    CharField
)
from django.contrib.auth import authenticate
from .models import User
from helper import helper


class AdminLoginSerializer(Serializer):
    email = CharField()
    password = CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_superuser:
            return user
        raise helper.exception.AuthenticationFailed()


class UserLoginSerializer(Serializer):
    email = CharField()
    password = CharField()

    def validate(self, data):
        user = authenticate(**data)

        if user and user.is_superuser:
            raise helper.exception.AuthenticationFailed()
        if user and user.is_verified:
            return user
        elif user and not user.is_verified:
            # user.otp = helper.generateOTP(6)
            user.otp = 123456
            user.save()
            # OTP to Mobile goes here...
            # raise helper.exception.PhoneNotVerified(
            #     helper.message.PHONE_NOT_VERIFIED)
            return user
        raise helper.exception.AuthenticationFailed()


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        user = User.objects.create_user(**data)
        # user.otp = helper.generateOTP(6)
        user.otp = 123456
        user.save()
        # Mobile OTP goes here

        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "otp", "is_staff"]

    