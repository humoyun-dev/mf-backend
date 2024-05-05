from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Order
from .serializers import OrderSerializer, OrderDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class OrderAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer



