from django.db import models

class CashDividend(models.Model):
    dividend_date = models.DateField()
    maturity_date = models.DateField()
    stock = models.ForeignKey("instruments.Stock", on_delete=models.CASCADE)
    coupon_no = models.CharField(max_length=50)
    coupon_value = models.DecimalField(max_digits=10, decimal_places=2)
    plus_day = models.BooleanField(default=False)

    def __str__(self):
        return f"Dividend ID: {self.id}, Stock: {self.stock}, Coupon No: {self.coupon_no}"
