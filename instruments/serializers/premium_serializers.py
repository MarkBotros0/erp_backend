from rest_framework import serializers
from ..models.premium import Premium, PremiumTransaction

class PremiumTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumTransaction
        fields = '__all__'

class PremiumSerializer(serializers.ModelSerializer):
    transactions = PremiumTransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Premium
        fields = '__all__'