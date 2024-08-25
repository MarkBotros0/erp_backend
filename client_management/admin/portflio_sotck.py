from django.contrib import admin

from client_management.models import PortfolioStock


@admin.register(PortfolioStock)
class PortfolioStockAdmin(admin.ModelAdmin):
    pass
