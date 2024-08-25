from rest_framework import serializers
from ..models.treasury_bill import TreasuryBill, TreasuryBillTrade

class TreasuryBillTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreasuryBillTrade
        fields = '__all__'

class TreasuryBillSerializer(serializers.ModelSerializer):
    trades = TreasuryBillTradeSerializer(many=True, read_only=True)

    class Meta:
        model = TreasuryBill
        fields = '__all__'