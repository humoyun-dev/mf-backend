# serializers.py
from rest_framework import serializers
from .models import Product, ProductImage, Proporties, Category

class CategorySerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    def get_product(self, obj):
        products = Product.objects.filter(category=obj.id)
        serializer = ProductSerializer(products, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ['id', 'name', 'product']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProportiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proporties
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    proporties = ProportiesSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
