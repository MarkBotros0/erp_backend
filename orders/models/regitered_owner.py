from django.db import models

# Omni-Bus
class RegisteredOwner(models.Model):

    # Part 1: Order Information
    entry_date = models.DateField(auto_now_add=True)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    broker_name = models.CharField(max_length=255)

    stock_name = models.CharField(max_length=255)
    executor_name = models.CharField(max_length=255)
    operation_type = models.CharField(max_length=10, choices=[('buy', 'شراء'), ( 'sell', 'بيع')])
    order_date = models.DateField()
    requested_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    client = models.ForeignKey('client_management.client', on_delete=models.CASCADE)
    portfolio = models.ForeignKey('client_management.portfolio', on_delete=models.CASCADE)
    client_requested_quantity = models.IntegerField()

    broker_invoice_number = models.CharField(max_length=100)
    executed_quantity = models.IntegerField()
    execution_value = models.DecimalField(max_digits=15, decimal_places=2)
    commissions = models.DecimalField(max_digits=10, decimal_places=2)
    total_invoice_amount = models.DecimalField(max_digits=15, decimal_places=2)
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=4)
    execution_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    average_execution_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_number} - {self.client_name}"

