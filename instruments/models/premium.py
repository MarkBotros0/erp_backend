# erp-project/backend/instruments/models/premium.py
from django.db import models


class Premium(models.Model):
    premium_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class PremiumTransaction(models.Model):
    premium = models.ForeignKey(Premium, on_delete=models.CASCADE, related_name='transactions')
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    client = models.ForeignKey('client_management.Client', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.premium.name} - {self.client.first_name} {self.client.family_name} - {self.transaction_date}"
