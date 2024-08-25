from django.contrib import admin

from client_management.models import BankBranch


@admin.register(BankBranch)
class BankBranchAdmin(admin.ModelAdmin):
    pass
