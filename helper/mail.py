from django.core.mail import send_mail
from django.conf import settings

def sendOTPMail(to, subject, message):
    return True
    # send_mail(subject, message, settings.EMAIL_HOST_USER, [to])