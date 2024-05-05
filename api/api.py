from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from orders.models import Order
from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView

class TotalIncomeAPIView(APIView):
    def get(self, request, format=None):
        # Calculate total income by summing up all total_price values from orders
        total_income = Order.objects.aggregate(total_income=models.Sum('total_price'))['total_income']

        # Return the total income in the response
        return Response({'total_income': total_income})
