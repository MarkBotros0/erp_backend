from rest_framework import viewsets
from ..models.treasury_bill import TreasuryBill, TreasuryBillTrade
from ..serializers.treasury_bill_serializers import TreasuryBillSerializer, TreasuryBillTradeSerializer

class TreasuryBillViewSet(viewsets.ModelViewSet):
    queryset = TreasuryBill.objects.all()
    serializer_class = TreasuryBillSerializer

class TreasuryBillTradeViewSet(viewsets.ModelViewSet):
    queryset = TreasuryBillTrade.objects.all()
    serializer_class = TreasuryBillTradeSerializer