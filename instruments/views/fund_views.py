from rest_framework import viewsets
from ..models.fund import Fund, FundType, FundTransaction, FundDividend
from ..serializers.fund_serializers import (
    FundSerializer, FundTypeSerializer, FundTransactionSerializer, FundDividendSerializer
)

class FundTypeViewSet(viewsets.ModelViewSet):
    queryset = FundType.objects.all()
    serializer_class = FundTypeSerializer

class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer

class FundTransactionViewSet(viewsets.ModelViewSet):
    queryset = FundTransaction.objects.all()
    serializer_class = FundTransactionSerializer

class FundDividendViewSet(viewsets.ModelViewSet):
    queryset = FundDividend.objects.all()
    serializer_class = FundDividendSerializer