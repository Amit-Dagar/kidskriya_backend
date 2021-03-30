from . import exception, encryption, message, permission, payment, mail, sms

from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from django.conf import settings
import requests
from random import randint
import os
import uuid

######### CUSTOM HELPER FUNCATIONS ###############

# Custom Response


def createResponse(message="", payload={}, status_code=status.HTTP_200_OK):
    return Response({"detail": message, "payload": payload}, status=status_code)


# Generate JWT token for user


def get_token(user):
    return api_settings.JWT_ENCODE_HANDLER(api_settings.JWT_PAYLOAD_HANDLER(user))


# Verify Google reCaptcha


def verify_recaptcha(request):
    status = (
        requests.post(
            settings.GOOGLE_VERIFY_RECAPTCHA_URL,
            data={
                "secret": settings.RECAPTCHA_SECRET_KEY,
                "response": request.data["g-recaptcha-response"],
            },
            verify=True,
        )
        .json()
        .get("success", False)
    )

    if not status:
        raise exception.NotAcceptable(message.INVALID_RECAPTCHA)

    return status


# Get Client IP Address


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


# Check Request has valid parameters


def check_parameters(request, params):
    if not all(param in request for param in params):
        raise exception.NotAcceptable(message.NOT_VALID_PARAMS)
    return True


# Generate OTP of length n


def generateOTP(length):
    length -= 1
    return randint(int("1" + "0" * length), int("9" + "9" * length))


# Is Empty


def isEmpty(var, name):
    if not var:
        raise exception.NotAcceptable(message.INVALID_INPUT(name))


# Unique Integer TimeStamp
def getUniqueId():
    id = uuid.uuid1()
    return id.node


# Modify phone number
def modifyPhoneNumber(phone):
    if "+" not in phone:
        if len(phone) == 10:
            phone = "+91" + phone
        else:
            raise exception.ParseError(message.INVALID_INPUT("Phone Number"))
    else:
        if len(phone) != 13:
            raise exception.ParseError(message.INVALID_INPUT("Phone Number"))
    try:
        int(phone)
    except Exception:
        raise exception.ParseError(message.INVALID_INPUT("Phone Number"))

    return phone
