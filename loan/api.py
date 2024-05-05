from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoansListSerializer, LoanDetailSerializer
from .models import Loan

class LoansListAPIView(APIView):
    def get(self, request):
        loans = Loan.objects.all()
        if loans.exists():
            serializer = LoansListSerializer(loans, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response({"error": "Laon Not Found"}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        serializer = LoanDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            loan = Loan.objects.get(pk=pk)
            serializer = LoanDetailSerializer(loan)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except loan.DoesNotExist:
            return Response({"error": "Loan Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        loan = Loan.objects.get(pk=pk)
        serializer = LoanDetailSerializer(loan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        loan = Loan.objects.get(pk=pk)
        loan.delete()
        return Response({"id": pk, "status":status.HTTP_200_OK, "deleted": True}, status=status.HTTP_200_OK)