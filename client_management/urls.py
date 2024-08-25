# erp-project\backend\client_management\urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from .views import ClientViewSet, ClientTitleViewSet, ClientTypeViewSet, ClientNatureViewSet, ClientFileUploadView

# router = DefaultRouter()
# router.register(r'clients', ClientViewSet)
# router.register(r'client-titles', ClientTitleViewSet)
# router.register(r'client-types', ClientTypeViewSet)
# router.register(r'client-natures', ClientNatureViewSet)

urlpatterns = [
   # path('', include(router.urls)),
    #path('upload/', ClientFileUploadView.as_view(), name='client-file-upload'),  # Added file upload path
]
