from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    DestroyAPIView,
)
from helper import helper
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer
from .models import Products
from schools.models import Schools, Classes


# CREATE PRODUCT
# POST
# PARAMS - school, cls, name, banner, price, stock, visibility
# /api/product/create
class CreateProduct(CreateAPIView):
    permission_classes = [helper.permission.IsAdmin]
    serializer_class = ProductSerializer

    def post(self, request):
        helper.check_parameters(
            request.data,
            ["school", "cls", "name", "banner", "price", "stock", "visibility"],
        )

        try:
            school = Schools.objects.get(id=request.data["school"])
        except Exception:
            raise helper.exception.NotAcceptable(
                helper.message.MODULE_NOT_FOUND("School")
            )

        try:
            cls = Classes.objects.get(id=request.data["cls"])
        except Exception:
            raise helper.exception.NotAcceptable(
                helper.message.MODULE_NOT_FOUND("Class")
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("Product", "created")
        )


# READ PRODUCTS
# get
# params(search) - ?search=<str>
# /api/product/read
# /api/product/read?search=
class ReadProduct(ListAPIView):
    def list(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = helper.settings.PAGE_SIZE

        if "search" in request.GET:
            if "school" in request.GET:
                if "class" in request.GET:
                    queryset = Products.objects.filter(
                        name__icontains=request.GET["search"],
                        school=request.GET["school"],
                        cls=request.GET["class"],
                    )
                else:
                    queryset = Products.objects.filter(
                        name__icontains=request.GET["search"],
                        school=request.GET["school"],
                    )
            else:
                if "class" in request.GET:
                    queryset = Products.objects.filter(
                        name__icontains=request.GET["search"],
                        cls=request.GET["class"],
                    )
                else:
                    queryset = Products.objects.filter(
                        name__icontains=request.GET["search"]
                    )
        else:
            if "school" in request.GET:
                if "class" in request.GET:
                    queryset = Products.objects.filter(
                        school=request.GET["school"],
                        cls=request.GET["class"],
                    )
                else:
                    queryset = Products.objects.filter(
                        school=request.GET["school"],
                    )
            else:
                if "class" in request.GET:
                    queryset = Products.objects.filter(
                        cls=request.GET["class"],
                    )
                else:
                    queryset = Products.objects.filter()

        page_context = paginator.paginate_queryset(queryset, request)

        return paginator.get_paginated_response(
            ProductSerializer(page_context, many=True).data
        )


# Update Product
# PUT
# PARAMS - school, cls, name, banner, price, discount, stock, visibility
# /api/product/update/<str:id>
class UpdateProduct(UpdateAPIView):
    permission_classes = [helper.permission.IsAdmin]

    def update(self, request, id):
        helper.check_parameters(
            request.data,
            [
                "school",
                "cls",
                "name",
                "banner",
                "price",
                "discount",
                "stock",
                "visibility",
            ],
        )

        try:
            product = Products.objects.get(id=id)
        except Exception as e:
            raise helper.exception.NotAcceptable(
                helper.message.MODULE_NOT_FOUND("Product")
            )
        try:
            school = Schools.objects.get(id=request.data["school"])
        except Exception:
            raise helper.exception.NotAcceptable(
                helper.message.MODULE_NOT_FOUND("School")
            )

        try:
            cls = Classes.objects.get(id=request.data["cls"])
        except Exception:
            raise helper.exception.NotAcceptable(
                helper.message.MODULE_NOT_FOUND("Class")
            )

        if request.data["banner"]:
            product.banner = request.FILES["banner"]

        product.name = request.data["name"]
        product.school = school
        product.cls = cls
        product.price = request.data["price"]
        product.stock = request.data["stock"]
        product.visibility = request.data["visibility"] in ["true", 1, True]

        product.save()

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("Product", "updated")
        )


# DELETE PRODUCT
# DELETE
# PARAMS -
# /api/product/delete/<str:id>
class DeleteProduct(DestroyAPIView):
    permission_classes = [helper.permission.IsAdmin]

    def delete(self, request, id):
        try:
            product = Products.objects.get(id=id)
        except Exception as e:
            raise helper.exception.NotAcceptable(
                helper.message.MODULE_NOT_FOUND("Product")
            )

        product.delete()

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("Product", "deleted")
        )
