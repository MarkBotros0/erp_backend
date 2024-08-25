from orders.models.order import Order
from django.contrib import admin


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
