from rest_framework.exceptions import *
from rest_framework import status
from .message import (
    NOT_ACCEPTABLE_REQUEST,
    EMAIL_NOT_VERIFIED,
    PHONE_NOT_VERIFIED
)


# EXCEPTIONS
class NotAcceptable(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_details = NOT_ACCEPTABLE_REQUEST
    default_code = NOT_ACCEPTABLE_REQUEST


# Exception for the codndition if email is not verfied by user
class EmailNotVerified(APIException):
    status = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_details = EMAIL_NOT_VERIFIED
    default_code = "email_not_verfied"


# Exception for the codndition if phone is not verfied by user
class PhoneNotVerified(APIException):
    status = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_details = PHONE_NOT_VERIFIED
    default_code = "email_not_verfied"
