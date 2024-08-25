from rest_framework import serializers
from ..models.call_account import CallAccount, CallAccountTransaction

class CallAccountTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallAccountTransaction
        fields = '__all__'

class CallAccountSerializer(serializers.ModelSerializer):
    transactions = CallAccountTransactionSerializer(many=True, read_only=True)

    class Meta:
        model = CallAccount
        fields = '__all__'