from rest_framework import viewsets
from ..models.deposit import Deposit, DepositTransaction
from ..serializers.deposit_serializers import DepositSerializer, DepositTransactionSerializer

class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

class DepositTransactionViewSet(viewsets.ModelViewSet):
    queryset = DepositTransaction.objects.all()
    serializer_class = DepositTransactionSerializer