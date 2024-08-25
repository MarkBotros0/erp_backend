from django.contrib import admin

from client_management.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
