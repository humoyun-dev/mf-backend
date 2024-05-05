from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Seller
from .serializers import SellerListSerializer, SellerDetailSerializer


class SellersListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sellers = Seller.objects.all()
        if sellers.exists():
            serializer = SellerListSerializer(sellers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No sellers found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = SellerListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SellerDetailAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            seller = Seller.objects.get(pk=pk)
            serializer = SellerDetailSerializer(seller)
            return Response(serializer.data)
        except seller.DoesNotExist:
            return Response({"error":"Seller not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        # Seller obyektini pk orqali olish
        seller = Seller.objects.get(pk=pk)
        # Yangi ma'lumotlarni o'qib olamiz
        serializer = SellerDetailSerializer(seller, data=request.data)
        if serializer.is_valid():
            # Ma'lumotlarni saqlaymiz
            serializer.save()
            # Yangilangan ma'lumotlarni qaytarish
            return Response(serializer.data)
        # Agar seriyalizatsiya noto'g'ri bo'lsa, xatoliklarni qaytarish
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        seller = Seller.objects.get(pk=pk)
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# hich qaysi kodimga tegma Humoyun