# erp-project/backend/instruments/models/call_account.py

from django.db import models


class CallAccount(models.Model):
    account_id = models.AutoField(primary_key=True)
    client = models.ForeignKey('client_management.Client', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=3)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    last_interest_calculation_date = models.DateField()

    def __str__(self):
        return f"Call Account {self.account_id} - {self.client.first_name} {self.client.family_name}"


class CallAccountTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdrawal'),
        ('INTEREST', 'Interest'),
    ]
    account = models.ForeignKey(CallAccount, on_delete=models.CASCADE, related_name='transactions')
    transaction_date = models.DateTimeField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.account.account_id} - {self.transaction_type} - {self.transaction_date}"
