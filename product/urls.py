from django.urls import path
from .api import ProductListAPIView, ProductShopDetailAPIView, ProductAddAPIView, CategoryListAPIView

urlpatterns = [
    path("", ProductListAPIView.as_view(), name='product-list'),
    path("shop/<int:shop_id>/", ProductShopDetailAPIView.as_view(), name='shop-product-list'),
    path("create/", ProductAddAPIView.as_view(), name='product_add'),
    path("category/", CategoryListAPIView.as_view(), name='category-list'),
]