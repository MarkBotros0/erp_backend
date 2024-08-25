# /erp-project/backend/instruments/serializers/stock_serializers.py

from rest_framework import serializers
from ..models import Stock, StockIssue, StockTrade, Sector, SubSector, StockExchange


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class SubSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSector
        fields = '__all__'


class StockExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockExchange
        fields = '__all__'


class StockIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockIssue
        fields = '__all__'


class StockTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTrade
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    sector = SectorSerializer(read_only=True)
    subsector = SubSectorSerializer(read_only=True)
    stock_exchange = StockExchangeSerializer(read_only=True)
    issues = StockIssueSerializer(many=True, read_only=True)
    trades = StockTradeSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = '__all__'
