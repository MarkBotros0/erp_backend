from django.db import models

from common.enums.currency import Currency


class StockIssue(models.Model):
    stock = models.ForeignKey("Stock", on_delete=models.CASCADE, related_name='issues')
    issue_date = models.DateField()
    currency = models.CharField(max_length=3, choices=Currency.get_choices())
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon = models.IntegerField(null=True, blank=True)
    is_internal = models.BooleanField(default=False)
    is_listed = models.BooleanField(default=False)
    book_keeping = models.BooleanField(default=False)
    bk_date = models.DateField()

    def __str__(self):
        return f"{self.stock.code} - Issue {self.issue_date}"
