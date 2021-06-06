from random import lognormvariate
from django.core import serializers
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
)
from helper import helper
from products.models import Products
from schools.models import Schools, Classes
from .models import Orders, OrderProducts
from .serializers import ReadOrderSerializer, OrderProductSerializer
import json


# CHECKOUT API
# POST
# params - products[]
# /api/order/checkout
class OrderPurchase(CreateAPIView):
    permission_classes = [helper.permission.IsAuthenticated]

    def post(self, request):
        helper.check_parameters(
            request.data, ["products", "school", "class", "address", "additional"]
        )
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
        school = request.data["school"]
        stu_class = request.data["class"]

        print(stu_class)

        if school:
            try:
                school = Schools.objects.get(id=school)
            except Exception:
                raise helper.exception.NotFound(
                    helper.message.MODULE_NOT_FOUND("School")
                )
        else:
            school = None

        # checking student_class
        if stu_class:
            try:
                stu_class = Classes.objects.get(id=stu_class)
            except Exception:
                raise helper.exception.NotFound(
                    helper.message.MODULE_NOT_FOUND("Class")
                )
        else:
            stu_class = None

        # create order
        order = Orders.objects.create(
            user=request.user,
            school=school,
            student_class=stu_class,
            price=price,
            status=1,
            address=request.data["address"],
            additional=request.data["additional"],
        )
        order.save()

        # preparing orders data
        products = ""
        for product in request.data["products"]:
            product_check = Products.objects.get(id=product)

            if product_check.stock == 1:
                msg = (
                    "Message: Product is out of stock \n\n product-name="
                    + product_check.name
                )
                helper.sms.sendTGMessage(msg)

            product_check.stock -= 1
            product_check.save()

            products = products + product_check.name + ", "

            orderProduct = OrderProducts.objects.create(
                order=order,
                user=request.user,
                product_name=product_check.name,
                product_price=product_check.price,
                discount=product_check.discount,
                banner=str(product_check.banner),
            )
            orderProduct.save()

        school = ""
        className = ""

        if order.school != None:
            school = order.school.name
        
        if order.student_class != None:
            className = order.student_class.name
        


        msgData = (
            "message: **New Order Placed**\n\n"
            + "orderId: "
            + str(order.id)
            + "\npayMethod: COD\nusername: "
            + order.user.name
            + "\nschool: "
            + school
            + "\nclass: "
            + className
            + "\nprice: "
            + str(order.price)
            + "\naddress: "
            + order.address
            + "\nadditionalDetails: "
            + order.additional
            + "\nstatus: Placed"
            + "\ncreated: "
            + str(order.created)
            + "\nproducts: "
            + products
        )

        helper.sms.sendTGMessage(msgData)

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("Order", "placed"),
            {"order_id": order.id},
        )


# Read All Orders
# GET
# /api/order/read
class ReadOrders(ListAPIView):
    permission_classes = [helper.permission.IsAuthenticated]
    http_method_names = ["get"]

    def list(self, request):
        user = request.user
        if user.is_superuser:
            queryset = Orders.objects.all()
        else:
            queryset = Orders.objects.filter(user=user)

        return helper.createResponse(
            helper.message.MODULE_LIST("Order"),
            ReadOrderSerializer(queryset, many=True).data,
        )


# Update Order
# GET
# /api/order/update/<str:id>
class UpdateOrder(UpdateAPIView):
    permission_classes = [helper.permission.IsAdmin]

    def update(self, request, id):
        helper.check_parameters(request.data, ["status"])
        order = helper.checkRecord(id, Orders, "Order")

        order.status = int(request.data["status"])
        order.save()

        serialized_obj = serializers.serialize(
            "json",
            [
                order,
            ],
        )
        status = "Placed"
        if order.status == 2:
            status = "Out for delivery"
        elif order.status == 3:
            status = "Delivered"

        productsData = OrderProductSerializer(
            OrderProducts.objects.filter(order_id=order.id), many=True
        ).data

        products = ""
        for pro in productsData:
            products = products + pro["product_name"] + ", "

        msgData = (
            "message: **Order Updated**\n\n"
            + "orderId: "
            + str(order.id)
            + "\npayMethod: COD\nusername: "
            + order.user.name
            + "\nschool: "
            + order.school.name
            + "\nclass: "
            + order.student_class.name
            + "\nprice: "
            + str(order.price)
            + "\naddress: "
            + order.address
            + "\nadditionalDetails: "
            + order.additional
            + "\nstatus: "
            + status
            + "\ncreated: "
            + str(order.created)
            + "\nproducts: "
            + products
        )

        helper.sms.sendTGMessage(msgData)

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("Order", "updated"),
            {"order_id": order.id},
        )
