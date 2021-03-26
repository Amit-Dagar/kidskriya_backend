from django.urls import path
from .api import (
    # SCHOOLS API
    CreateSchool,
    ReadSchools,
    UpdateSchool,
    DeleteSchool,
    # CLASSES
    CreateClass,
    ReadClasses,
    UpdateClass,
    DeleteClass,
)

urlpatterns = [
    # School API
    path("create", CreateSchool.as_view()),
    path("read", ReadSchools.as_view()),
    path("update/<str:id>", UpdateSchool.as_view()),
    path("delete/<str:id>", DeleteSchool.as_view()),
    # Class API
    path("class/create", CreateClass.as_view()),
    path("class/read", ReadClasses.as_view()),
    path("class/update/<str:id>", UpdateClass.as_view()),
    path("class/delete/<str:id>", DeleteClass.as_view()),
]
