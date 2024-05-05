from django.core import serializers
from rest_framework import serializers
from .models import Loan


class LoansListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ["id", "loan_name", "loan_value", "get_loan_date", 'give_loan_date', "owner"]


class LoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ["loan_name", "loan_value", "get_loan_date", 'give_loan_date', "owner"]