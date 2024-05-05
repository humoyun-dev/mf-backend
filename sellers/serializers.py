from rest_framework import serializers
from .models import Seller

class SellerListSerializer(serializers.ModelSerializer):
    # owner = serializers.CharField(source='owner.auth_token.key', read_only=True)
    class Meta:
        model = Seller
        fields = ["pk", "first_name", "last_name", "phone_number", "password", "profile_picture"]

class SellerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"