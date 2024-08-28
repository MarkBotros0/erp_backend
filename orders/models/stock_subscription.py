from django.db import models
from orders.enum.subscription_types import SubscriptionType

class StockSubscription(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    stock = models.ForeignKey('instruments.Stock', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    installment = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField()
    bank = models.ForeignKey('client_management.Bank', on_delete=models.CASCADE)
    bank_branch = models.ForeignKey('client_management.BankBranch', on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=10, choices=SubscriptionType.choices(), default=SubscriptionType.GENERAL.value)
    qty_for_persons_min = models.PositiveIntegerField(null=True, blank=True)
    qty_for_persons_max = models.PositiveIntegerField(null=True, blank=True)
    qty_for_companies_min = models.PositiveIntegerField(null=True, blank=True)
    qty_for_companies_max = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Subscription {self.id} for {self.stock.name}"
