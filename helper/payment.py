from django.conf import settings
import razorpay

client = razorpay.Client(auth=(settings.RPAY_KEY, settings.RPAY_SECRET))


def razorpay(data):
    return client.order.create(data=data)