from django.urls import path
from .api import (
    CreateProduct,
    ReadProduct,
    UpdateProduct,
    DeleteProduct
)

urlpatterns = [
    path('create', CreateProduct.as_view()),
    path('read', ReadProduct.as_view()),
    path('update/<str:id>', UpdateProduct.as_view()),
    path('delete/<str:id>', DeleteProduct.as_view()),
]