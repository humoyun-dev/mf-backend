from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductSerializer
from rest_framework.response import Response
from .models import Product ,Category ,ProductImage, Proporties

class ProductListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(owner=user)

class ProductShopDetailAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        self.shop_id = self.kwargs['shop_id']

        return Product.objects.filter(owner=user, shop_id=self.shop_id)

class ProductAddAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # Ensure that the token is present and has a user associated with it
        if not request.auth or not request.auth.user:
            return Response({'detail': 'Invalid or missing token.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Extract user from the token
        user = request.auth.user

        # Create a mutable copy of the QueryDict
        mutable_data = request.data.copy()

        # Set the user field in the mutable data to the authenticated user
        mutable_data['owner'] = user.id

        # Continue with your logic to create a new order
        serializer = ProductSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)