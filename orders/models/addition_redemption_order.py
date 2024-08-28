from django.db import models


class AdditionRedemptionOrder(models.Model):
    order = models.ForeignKey('orders.order', on_delete=models.CASCADE)
    order_date = models.DateField()
    client = models.ForeignKey('client_management.client', on_delete=models.CASCADE)
    portfolio = models.ForeignKey('client_management.portfolio', on_delete=models.CASCADE)
    stock = models.ForeignKey('instruments.Stock', on_delete=models.CASCADE)
    custodian = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('ADDITION', 'Addition'),('REDEMPTION', 'Redemption')])
    capital_effect = models.BooleanField(default=False)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.order} - {self.client}"
