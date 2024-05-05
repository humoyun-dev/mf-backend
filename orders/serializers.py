from rest_framework import serializers
from .models import Order, ProductOrder
class ProductOrderSerializer(serializers.ModelSerializer):
    # product_data = ProductDetailSerializer(source="product", read_only=True,)

    class Meta:
        model = ProductOrder
        fields = ['price', 'quantity', 'price', "product_data"]


class OrderSerializer(serializers.ModelSerializer):
    products = ProductOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", 'name', 'phone_number', 'owner', 'total_price', 'products']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        total_price = 0
        for product_data in products_data:
            product = product_data['product']
            price = product_data['price']
            quantity = product_data['quantity']
            total_price += price * quantity
            ProductOrder.objects.create(order=order, product=product, price=price, quantity=quantity)
        order.total_price = total_price
        order.save()
        return order

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products')
        instance = super().update(instance, validated_data)
        total_price = 0
        instance.products.all().delete()
        for product_data in products_data:
            product = product_data['product']
            price = product_data['price']
            quantity = product_data['quantity']
            total_price += price * quantity
            ProductOrder.objects.create(order=instance, product=product, price=price, quantity=quantity)
        instance.total_price = total_price
        instance.save()
        return instance

class OrderDetailSerializer(serializers.ModelSerializer):
    products = ProductOrderSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ["id", "name", "phone_number", "owner", "total_price", "products"]