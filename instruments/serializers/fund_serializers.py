from rest_framework import serializers
from ..models.fund import Fund, FundType, FundTransaction, FundDividend

class FundTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundType
        fields = '__all__'

class FundTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundTransaction
        fields = '__all__'

class FundDividendSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundDividend
        fields = '__all__'

class FundSerializer(serializers.ModelSerializer):
    fund_type = FundTypeSerializer(read_only=True)
    transactions = FundTransactionSerializer(many=True, read_only=True)
    dividends = FundDividendSerializer(many=True, read_only=True)

    class Meta:
        model = Fund
        fields = '__all__'