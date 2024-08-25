from django.contrib import admin

from client_management.models import InvestmentType


@admin.register(InvestmentType)
class InvestmentTypeAdmin(admin.ModelAdmin):
    pass
