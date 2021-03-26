from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView
)
from .serializers import (
    AdminLoginSerializer,
    UserLoginSerializer,
    UserSignupSerializer,
    authenticate
)
from .models import User
from helper import helper

# Admin Login API


class AdminLogin(GenericAPIView):
    serializer_class = AdminLoginSerializer

    def post(self, request):
        helper.check_parameters(request.data, ['phone', 'password'])

        data = {
            "phone": helper.modifyPhoneNumber(request.data['phone']),
            "password": request.data['password']
        }

        user = self.get_serializer(data=data)
        user.is_valid(raise_exception=True)
        user = user.validated_data

        return helper.createResponse(
            helper.message.LOGIN_SUCCESS,
            {
                "user": user.name,
                "email": user.email,
                "token": helper.get_token(user)
            }
        )


# User Login API
class UserLogin(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        helper.check_parameters(request.data, ['phone', 'password'])

        data = {
            "phone": helper.modifyPhoneNumber(request.data['phone']),
            "password": request.data['password']
        }

        user = self.get_serializer(data=data)
        user.is_valid(raise_exception=True)
        user = user.validated_data

        return helper.createResponse(
            helper.message.LOGIN_SUCCESS,
            {
                "user": user.name,
                "token": helper.get_token(user)
            }
        )


# User Signup API
class UserSignup(CreateAPIView):
    serializer_class = UserSignupSerializer

    def post(self, request):
        helper.check_parameters(request.data, ['name', 'phone', 'password'])

        phone = helper.modifyPhoneNumber(request.data['phone'])

        if User.objects.filter(phone=phone).count() > 0:
            raise helper.exception.NotAcceptable(
                helper.message.USER_PHONE_EXISTS)

        user = self.get_serializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()

        return helper.createResponse(helper.message.SIGNUP_USER_SUCCESS)


# User Confirm OTP API
class ConfirmOTP(CreateAPIView):
    def post(self, request):
        helper.check_parameters(request.data, ['phone', 'otp'])
        phone = helper.modifyPhoneNumber(request.data['phone'])
        try:
            user = User.objects.get(
                phone=phone, otp=request.data['otp'])
        except Exception:
            raise helper.exception.NotFound(helper.message.VERIFY_OTP_MISMATCH)

        user.otp = None
        user.is_verified = True
        user.save()

        return helper.createResponse(
            helper.message.VERIFY_PHONE_SUCCESS,
            {
                "user": user.name,
                "token": helper.get_token(user)
            }
        )


# Forgot Password API
class ForgotPassword(CreateAPIView):
    def post(self, request):
        helper.check_parameters(request.data, ['phone'])

        phone = helper.modifyPhoneNumber(request.data['phone'])

        try:
            user = User.objects.get(phone=phone)
        except Exception as e:
            raise helper.exception.NotFound(
                helper.message.MODULE_NOT_FOUND('user'))

        user.otp = helper.generateOTP(6)
        user.save()
        message = "You OTP (" + str(user.otp) + \
            ") for verification at KidsKriya. Thank you choosing us"
        helper.sms.sendSMS(user.phone, message)

        return helper.createResponse(helper.message.FORGOT_PASSWORD_SUCCESS)


# Reset Password API
class ResetPassword(CreateAPIView):
    def post(self, request):
        helper.check_parameters(request.data, ['otp', 'phone', 'new_password'])

        phone = helper.modifyPhoneNumber(request.data['phone'])
        try:
            user = User.objects.get(phone=phone, otp=request.data['otp'])
        except Exception as e:
            raise helper.exception.NotFound(helper.message.VERIFY_OTP_MISMATCH)

        user.otp = None
        user.set_password(request.data['new_password'])
        user.save()

        return helper.createResponse(helper.message.RESET_PASSWORD_SUCCESS)


# Update Password
class UpdatePassword(CreateAPIView):
    permission_classes = [helper.permission.IsAuthenticated]
    serializer_class = UserLoginSerializer

    def post(self, request):
        helper.check_parameters(request.data, ["old_password", "new_password"])
        helper.isEmpty(request.data["old_password"], "old_password")

        user = authenticate(
            **{
                "username": request.user.username,
                "password": request.data["old_password"],
            }
        )

        if user != None:
            user.set_password(request.data["new_password"])
            user.save()
            return helper.createResponse(helper.message.CHANGE_PASSWORD_SUCCESS)
        else:
            return helper.createResponse(helper.message.PASSWORD_MISMATCH)
