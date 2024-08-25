from django.contrib import admin

from client_management.models import ClientTitle


@admin.register(ClientTitle)
class ClientTitleAdmin(admin.ModelAdmin):
    pass
