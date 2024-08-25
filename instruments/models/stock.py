# erp-project/backend/instruments/models/stock.py

from django.db import models


class Stock(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20, blank=True)
    sector = models.ForeignKey("Sector", on_delete=models.SET_NULL, null=True)
    sub_sector = models.ForeignKey("SubSector", on_delete=models.SET_NULL, null=True)
    stock_exchange = models.ForeignKey("StockExchange", on_delete=models.SET_NULL, null=True)
    foreign_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    number_of_shares = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    egypt_value = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
