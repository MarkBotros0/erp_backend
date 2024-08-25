from rest_framework import viewsets
from ..models import Stock, StockIssue, StockTrade, Sector, SubSector, StockExchange
from ..serializers.stock_serializers import (
    StockSerializer, StockIssueSerializer, StockTradeSerializer,
    SectorSerializer, SubSectorSerializer, StockExchangeSerializer
)


class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class SubSectorViewSet(viewsets.ModelViewSet):
    queryset = SubSector.objects.all()
    serializer_class = SubSectorSerializer


class StockExchangeViewSet(viewsets.ModelViewSet):
    queryset = StockExchange.objects.all()
    serializer_class = StockExchangeSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockIssueViewSet(viewsets.ModelViewSet):
    queryset = StockIssue.objects.all()
    serializer_class = StockIssueSerializer


class StockTradeViewSet(viewsets.ModelViewSet):
    queryset = StockTrade.objects.all()
    serializer_class = StockTradeSerializer
