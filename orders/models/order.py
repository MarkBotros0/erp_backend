from django.db import models

from common.models import TimestampsAbstractModel

class Order(TimestampsAbstractModel):
    order_date = models.DateField()
    broker = models.CharField(max_length=255)
    dealer = models.CharField(max_length=255)
    stock = models.ForeignKey("instruments.Stock", on_delete=models.CASCADE)
    bkeeper = models.CharField(max_length=255)
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
    type_order = models.CharField(max_length=50)
    marketing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deal_price = models.DecimalField(max_digits=10, decimal_places=2)
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                    blank=True)
    is_margin = models.BooleanField(default=False, verbose_name='Is margin')
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Percentage, optional
    same_day = models.BooleanField(default=False)
    portfolio = models.ForeignKey('client_management.Portfolio', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    executed_quantity = models.IntegerField(default=0)
    order_value = models.DecimalField(max_digits=15, decimal_places=2)
    safety_factor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.broker}"
