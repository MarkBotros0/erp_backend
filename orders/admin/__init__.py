from .order_admin import OrderAdmin
__all__ = ['OrderAdmin']

from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

app = apps.get_app_config('orders')
for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

