from rest_framework import viewsets
from ..models.premium import Premium, PremiumTransaction
from ..serializers.premium_serializers import PremiumSerializer, PremiumTransactionSerializer

class PremiumViewSet(viewsets.ModelViewSet):
    queryset = Premium.objects.all()
    serializer_class = PremiumSerializer

class PremiumTransactionViewSet(viewsets.ModelViewSet):
    queryset = PremiumTransaction.objects.all()
    serializer_class = PremiumTransactionSerializer