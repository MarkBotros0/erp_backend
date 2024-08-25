from django.db import models

from common.models import TimestampsAbstractModel


class StockPrice(TimestampsAbstractModel):
    stock = models.ForeignKey(
        "instruments.Stock", on_delete=models.CASCADE, related_name="prices"
    )
    summary_date = models.DateField()
    day_open_price = models.FloatField()
    day_close_price = models.FloatField()
    day_highest_price = models.FloatField()
    day_lowest_price = models.FloatField()
    trade_volume = models.FloatField()

    def __str__(self):
        return f"{self.summary_date} - {self.stock}"

    class Meta:
        unique_together = ["symbol", "summary_date"]
