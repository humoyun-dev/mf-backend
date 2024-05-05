from rest_framework import serializers
from orders.models import Order

class Total(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['total_price']


#
# class ProductOrderSerializer(serializers.ModelSerializer):
#     # product_data = ProductDetailSerializer(source="product", read_only=True,)
#
#     class Meta:
#         model = ProductOrder
#         fields = ['price', 'quantity', 'price', "product_data"]
#
#
# class OrderSerializer(serializers.ModelSerializer):
#     products = ProductOrderSerializer(many=True, read_only=True)
#     class Meta:
#         model = Order
#         fields = ["id", 'name', 'phone_number', 'owner', 'total_price', 'products']
# class OrderDetailSerializer(serializers.ModelSerializer):
#     products = ProductOrderSerializer(many=True, read_only=True)
#     class Meta:
#         model = Order
#         fields = ["id", "name", "phone_number", "owner", "total_price", "products"]