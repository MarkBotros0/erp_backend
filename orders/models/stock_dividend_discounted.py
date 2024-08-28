from django.db import models

from orders.enum.stock_type import StockType

class StockDividendDiscounted(models.Model):
    dividend_id = models.ForeignKey('orders.CashDividend', on_delete=models.CASCADE)
    dividend_date = models.DateField()
    maturity_date = models.DateField()
    stock = models.ForeignKey('instruments.Stock', on_delete=models.CASCADE)
    ratio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_type = models.CharField(max_length=50, choices=StockType.choices())
    bank = models.ForeignKey('client_management.Bank', on_delete=models.CASCADE)
    branch = models.ForeignKey('client_management.BankBranch', on_delete=models.CASCADE)

    def __str__(self):
        return f"StockDividendDiscounted: (divId:{self.dividend_id} - {self.stock})"
