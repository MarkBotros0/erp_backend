# erp-project/backend/instruments/models/treasury_bill.py

from django.db import models


class TreasuryBill(models.Model):
    tbill_id = models.AutoField(primary_key=True)
    issue_date = models.DateField()
    maturity_date = models.DateField()
    face_value = models.DecimalField(max_digits=15, decimal_places=2)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f"T-Bill {self.tbill_id} - {self.issue_date} to {self.maturity_date}"


class TreasuryBillTrade(models.Model):
    TRADE_TYPES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]
    tbill = models.ForeignKey(TreasuryBill, on_delete=models.CASCADE, related_name='trades')
    trade_date = models.DateTimeField()
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tbill.tbill_id} - {self.trade_type} - {self.trade_date}"
