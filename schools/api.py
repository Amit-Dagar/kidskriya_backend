from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializers import SchoolSerializer, ClassSerializer
from .models import Schools, Classes
from helper import helper

# ############## SCHOOLS API ############## #


# Create School
# POST
# PARAMS - name, city, state, pin, address, phone, email
# /api/school/create
class CreateSchool(CreateAPIView):
    permission_classes = [helper.permission.IsAdmin]
    serializer_class = SchoolSerializer

    def post(self, request):
        helper.check_parameters(
            request.data, ["name", "city", "state", "pin", "address", "phone", "email"]
        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("School", "created")
        )


# Read Schools List
# GET
# PARAMS -
# /api/school/read
class ReadSchools(ListAPIView):
    http_method_names = ["get"]

    def list(self, request):
        queryset = Schools.objects.all()

        return helper.createResponse(
            helper.message.MODULE_LIST("School"),
            SchoolSerializer(queryset, many=True).data,
        )


# Update School
# PUT
# PARAMS - name, city, state, pin, address, phone, email
# /api/school/update/<str:id>
class UpdateSchool(UpdateAPIView):
    permission_classes = [helper.permission.IsAdmin]

    def update(self, request, id):
        helper.check_parameters(
            request.data, ["name", "city", "state", "pin", "address", "phone", "email"]
        )

        try:
            school = Schools.objects.get(id=id)
        except Exception as e:
            raise helper.exception.NotAcceptable(
                helper.message.MODULE_NOT_FOUND("School")
            )

        school.name = request.data["name"]
        school.city = request.data["city"]
        school.state = request.data["state"]
        school.pin = request.data["pin"]
        school.address = request.data["address"]
        school.phone = request.data["phone"]
        school.email = request.data["email"]

        school.save()

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("School", "updated")
        )


# DELETE School
# DELETE
# PARAMS -
# /api/school/delete/<str:id>
class DeleteSchool(DestroyAPIView):
    permission_classes = [helper.permission.IsAdmin]

    def delete(self, request, id):
        try:
            school = Schools.objects.get(id=id)
        except Exception as e:
            raise helper.exception.NotAcceptable(
                helper.message.MODULE_NOT_FOUND("School")
            )

        school.delete()

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("School", "deleted")
        )


# ############## CLASSES API ############## #

# Create Class
# POST
# PARAMS - name
# /api/school/class/create
class CreateClass(CreateAPIView):
    permission_classes = [helper.permission.IsAdmin]
    serializer_class = ClassSerializer

    def post(self, request):
        helper.check_parameters(
            request.data, ["name"]
        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("Class", "created")
        )


# Read Class List
# GET
# PARAMS -
# /api/school/class/read
class ReadClasses(ListAPIView):
    http_method_names = ["get"]

    def list(self, request):
        queryset = Classes.objects.all()

        return helper.createResponse(
            helper.message.MODULE_LIST("Class"),
            ClassSerializer(queryset, many=True).data,
        )


# Update Class
# PUT
# PARAMS - name
# /api/school/class/update/<str:id>
class UpdateClass(UpdateAPIView):
    permission_classes = [helper.permission.IsAdmin]

    def update(self, request, id):
        helper.check_parameters(
            request.data, ["name"]
        )

        try:
            classes = Classes.objects.get(id=id)
        except Exception as e:
            raise helper.exception.NotAcceptable(
                helper.message.MODULE_NOT_FOUND("Class")
            )

        classes.name = request.data["name"]

        classes.save()

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("Class", "updated")
        )


# DELETE Class
# DELETE
# PARAMS -
# /api/school/class/delete/<str:id>
class DeleteClass(DestroyAPIView):
    permission_classes = [helper.permission.IsAdmin]

    def delete(self, request, id):
        try:
            classes = Classes.objects.get(id=id)
        except Exception as e:
            raise helper.exception.NotAcceptable(
                helper.message.MODULE_NOT_FOUND("Class")
            )

        classes.delete()

        return helper.createResponse(
            helper.message.MODULE_STATUS_CHANGE("Class", "deleted")
        )
