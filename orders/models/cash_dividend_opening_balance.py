from django.db import models

class CashDividendOpeningBalance(models.Model):
    trans_id = models.AutoField(primary_key=True)
    trans_date = models.DateField()
    portfolio = models.ForeignKey('client_management.Portfolio', on_delete=models.CASCADE)
    client = models.ForeignKey('client_management.Client', on_delete=models.CASCADE)
    div_id = models.ForeignKey('orders.CashDividend', on_delete=models.CASCADE)
    stock = models.ForeignKey('instruments.Stock', on_delete=models.CASCADE)
    coupon_no = models.CharField(max_length=50)
    date = models.DateField()
    div_value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    bkeeper = models.CharField(max_length=255)
    quantity = models.IntegerField()
    cash_value = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Trans ID: {self.trans_id}, Portfolio: {self.portfolio}, Div ID: {self.div_id}"