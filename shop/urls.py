from django.urls import path
from .api import ShopListAPI, ShopAddAPI, ShopDetailAPI

urlpatterns = [
    path('', ShopListAPI.as_view(), name='shop_list'),
    path('create/', ShopAddAPI.as_view(), name='shop_create'),
    path('<int:pk>/', ShopDetailAPI.as_view(), name='shop_detail'),
]