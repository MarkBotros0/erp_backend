from django.db import models

class StockSplit(models.Model):
    split_date = models.DateField()
    stock = models.ForeignKey('instruments.Stock', on_delete=models.CASCADE)
    ratio = models.DecimalField(max_digits=10, decimal_places=4)
    bank = models.ForeignKey('client_management.Bank', on_delete=models.CASCADE)
    bank_branch = models.ForeignKey('client_management.BankBranch', on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Stock Split: {self.id} for stockId:{self.stock}"
