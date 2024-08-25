# erp-project/backend/instruments/models/bond.py

from django.db import models

from instruments.enums.trade_type import TradeType


class BondType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Bond(models.Model):
    bond_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20, blank=True)
    issue_date = models.DateField()
    subscription_close_date = models.DateField()
    maturity_date = models.DateField()
    currency = models.CharField(max_length=3)
    bond_type = models.ForeignKey(BondType, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quota = models.PositiveIntegerField()
    is_bookkeeping = models.BooleanField(default=False)
    bookkeeping_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.bond_id})"


class BondCoupon(models.Model):
    bond = models.ForeignKey(Bond, on_delete=models.CASCADE, related_name='coupons')
    coupon_date = models.DateField()
    coupon_rate = models.DecimalField(max_digits=5, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bond.name} - Coupon {self.coupon_date}"


class BondTrade(models.Model):
    bond = models.ForeignKey(Bond, on_delete=models.CASCADE, related_name='trades')
    trade_date = models.DateTimeField()
    trade_type = models.CharField(max_length=4, choices=TradeType.get_choices())
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.bond.name} - {self.trade_type} - {self.trade_date}"
