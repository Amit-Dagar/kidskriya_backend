from rest_framework.serializers import ModelSerializer
from .models import Schools, Classes


# School Serializer
class SchoolSerializer(ModelSerializer):
    class Meta:
        model = Schools
        fields = "__all__"


# Class Serializer
class ClassSerializer(ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"
