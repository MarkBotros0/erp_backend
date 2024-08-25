from rest_framework import serializers
from ..models.bond import Bond, BondType, BondCoupon, BondTrade

class BondTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BondType
        fields = '__all__'

class BondCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = BondCoupon
        fields = '__all__'

class BondTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BondTrade
        fields = '__all__'

class BondSerializer(serializers.ModelSerializer):
    bond_type = BondTypeSerializer(read_only=True)
    coupons = BondCouponSerializer(many=True, read_only=True)
    trades = BondTradeSerializer(many=True, read_only=True)

    class Meta:
        model = Bond
        fields = '__all__'