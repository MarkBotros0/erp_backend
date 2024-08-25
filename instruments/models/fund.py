# erp-project/backend/instruments/models/fund.py

from django.db import models


class FundType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Fund(models.Model):
    fund_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    fund_type = models.ForeignKey(FundType, on_delete=models.PROTECT)
    inception_date = models.DateField()
    nav = models.DecimalField(max_digits=15, decimal_places=2)  # Net Asset Value
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} ({self.fund_id})"


class FundTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('SUBSCRIPTION', 'Subscription'),
        ('REDEMPTION', 'Redemption'),
    ]
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name='transactions')
    client = models.ForeignKey('client_management.Client', on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    units = models.DecimalField(max_digits=15, decimal_places=4)

    def __str__(self):
        return f"{self.fund.name} - {self.client.first_name} {self.client.family_name} - {self.transaction_type} - {self.transaction_date}"


class FundDividend(models.Model):
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name='dividends')
    declaration_date = models.DateField()
    ex_date = models.DateField()
    payment_date = models.DateField()
    amount_per_unit = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.fund.name} - Dividend {self.declaration_date}"
