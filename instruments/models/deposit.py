# erp-project/backend/instruments/models/deposit.py

from django.db import models

from common.models import TimestampsAbstractModel


class Deposit(TimestampsAbstractModel):
    client = models.ForeignKey('client_management.Client', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=3)
    start_date = models.DateField()
    end_date = models.DateField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    is_auto_renewable = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[
        ('ACTIVE', 'Active'),
        ('MATURED', 'Matured'),
        ('LIQUIDATED', 'Liquidated'),
    ])

    def __str__(self):
        return f"Deposit {self.id} - {self.client.first_name} {self.client.family_name}"


class DepositTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('ISSUE', 'Issue'),
        ('SETTLE', 'Settle'),
        ('DECREASE', 'Decrease'),
        ('LIQUIDATE', 'Liquidate'),
        ('RENEW', 'Renew'),
    ]
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE, related_name='transactions')
    transaction_date = models.DateTimeField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.deposit.deposit_id} - {self.transaction_type} - {self.transaction_date}"
