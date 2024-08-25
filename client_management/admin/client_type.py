from django.contrib import admin

from client_management.models import ClientType


@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    pass
