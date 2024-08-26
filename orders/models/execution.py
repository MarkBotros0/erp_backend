from django.db import models
from common.models import TimestampsAbstractModel


class Execution(TimestampsAbstractModel):
    invoice_no = models.CharField(max_length=20)
    execution_value = models.IntegerField()
    order = models.ForeignKey('orders.order',on_delete=models.CASCADE)


    def __str__(self):
        return f"Execution {self.id}"
