from django.db import models

from instruments.enums.trade_type import TradeType


class StockTrade(models.Model):
    stock = models.ForeignKey("Stock", on_delete=models.CASCADE, related_name='trades')
    quantity = models.PositiveIntegerField()
    trade_date = models.DateTimeField()
    trade_type = models.CharField(max_length=4, choices=TradeType.get_choices())
    price = models.DecimalField(max_digits=10, decimal_places=2)
    portfolio = models.ForeignKey("client_management.Portfolio", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.stock.code} - {self.trade_type} - {self.trade_date}"
