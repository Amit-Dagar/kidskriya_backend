from django.urls import path
from .api import (
    AdminLogin,
    UserLogin,
    UserSignup,
    ConfirmOTP,
    ForgotPassword,
    ResetPassword,
    UpdatePassword,
    ReadUser
)


urlpatterns = [
    path('adminLogin', AdminLogin.as_view()),
    path('login', UserLogin.as_view()),
    path('signup', UserSignup.as_view()),
    path('confirm', ConfirmOTP.as_view()),
    path('forgotPassword', ForgotPassword.as_view()),
    path('resetPassword', ResetPassword.as_view()),
    path('updatePassword', UpdatePassword.as_view()),
    path('readUsers', ReadUser.as_view()),
]