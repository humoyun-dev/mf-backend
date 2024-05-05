from rest_framework import serializers
from .models import CustomUser, Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['status_name', 'price', 'id']

class CustomUserSerializer(serializers.ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'id', 'status', 'phone_number', 'profile_image', 'last_login']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class CustomUserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    verification_code = serializers.CharField()
    password = serializers.CharField(required=True)
