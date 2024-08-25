from django.contrib import admin

from client_management.models import ClientNature


@admin.register(ClientNature)
class ClientNatureAdmin(admin.ModelAdmin):
    pass
