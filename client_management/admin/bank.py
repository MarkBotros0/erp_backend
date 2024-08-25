from django.contrib import admin

from client_management.models import Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    pass
