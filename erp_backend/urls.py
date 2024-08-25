from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/client-management/', include('client_management.urls')),
    path('api/instruments/', include('instruments.urls')),
]