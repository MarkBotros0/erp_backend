from rest_framework import serializers
from ..models.deposit import Deposit, DepositTransaction

class DepositTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositTransaction
        fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
    transactions = DepositTransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Deposit
        fields = '__all__'