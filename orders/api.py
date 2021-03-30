from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from helper import helper
from rest_framework.pagination import PageNumberPagination
from products.models import Products
from schools.models import Schools, Classes
from .models import Orders, OrderProducts
from .serializers import OrderSerializer, OrderProductSerializer


# CHECKOUT API
# POST
# params - products[]
# /api/order/checkout
class OrderPurchase(CreateAPIView):
    permission_classes = [helper.permission.IsAuthenticated]

    def post(self, request):
        helper.check_parameters(request.data, ["products", "school", "class"])
        price = 0

        # checking all products are valid or not
        for product in request.data["products"]:
            try:
                product_check = Products.objects.get(id=product)

                if product_check.discount != 0:
                    price += product_check.price - (
                        (product_check.price * product_check.discount) / 100
                    )
                else:
                    price += product_check.price

            except Exception:
                raise helper.exception.ParseError(helper.message.UNKNOWN_ERR)

        # checking school
        try:
            school = Schools.objects.get(id=request.data["school"])
        except Exception:
            raise helper.exception.NotFound(helper.message.MODULE_NOT_FOUND("School"))

        # checking student_class
        try:
            stu_class = Classes.objects.get(id=request.data["class"])
        except Exception:
            raise helper.exception.NotFound(helper.message.MODULE_NOT_FOUND("Class"))

        # create order
        order = Orders.objects.create(
            user=request.user,
            school=school,
            student_class=stu_class,
            price=price,
            status=1,
        )
        order.save()

        data = {
            "amount": int(price * 100),
            "currency": "INR",
            "receipt": str(order.id),
            # "notes": {"order_id": str(order.id), "username": request.user.name},
        }
        response = helper.payment.razorpay(data)
        order.payment_id=response['id']
        order.save()

        # preparing orders data
        for product in request.data["products"]:
            product_check = Products.objects.get(id=product)

            orderProduct = OrderProducts.objects.create(
                order=order,
                user=request.user,
                product_name=product_check.name,
                product_price=product_check.price,
                discount=product_check.discount,
                banner=str(product_check.banner),
            )
            orderProduct.save()

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("Order", "created"),
            {
                "order_id": order.payment_id
            }
        )
