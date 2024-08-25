from django.db import models


class BankBranch(models.Model):
    name = models.CharField(max_length=20)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bank.name} - {self.name}"
