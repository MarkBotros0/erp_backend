from rest_framework import viewsets
from ..models.call_account import CallAccount, CallAccountTransaction
from ..serializers.call_account_serializers import CallAccountSerializer, CallAccountTransactionSerializer

class CallAccountViewSet(viewsets.ModelViewSet):
    queryset = CallAccount.objects.all()
    serializer_class = CallAccountSerializer

class CallAccountTransactionViewSet(viewsets.ModelViewSet):
    queryset = CallAccountTransaction.objects.all()
    serializer_class = CallAccountTransactionSerializer