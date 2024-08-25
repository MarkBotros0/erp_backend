from rest_framework import viewsets
from ..models.bond import Bond, BondType, BondCoupon, BondTrade
from ..serializers.bond_serializers import (
    BondSerializer, BondTypeSerializer, BondCouponSerializer, BondTradeSerializer
)

class BondTypeViewSet(viewsets.ModelViewSet):
    queryset = BondType.objects.all()
    serializer_class = BondTypeSerializer

class BondViewSet(viewsets.ModelViewSet):
    queryset = Bond.objects.all()
    serializer_class = BondSerializer

class BondCouponViewSet(viewsets.ModelViewSet):
    queryset = BondCoupon.objects.all()
    serializer_class = BondCouponSerializer

class BondTradeViewSet(viewsets.ModelViewSet):
    queryset = BondTrade.objects.all()
    serializer_class = BondTradeSerializer