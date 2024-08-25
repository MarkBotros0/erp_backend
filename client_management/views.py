# erp-project\backend\client_management\views.py

# views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
import logging
from .models import Client, ClientTitle, ClientType, ClientNature
from .serializers import ClientSerializer, ClientTitleSerializer, ClientTypeSerializer, ClientNatureSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .file_upload_handler import handle_uploaded_file

# Set up logging
logger = logging.getLogger(__name__)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            logger.debug("Client list retrieved successfully.")
            return response
        except Exception as e:
            logger.error(f"Error retrieving client list: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            logger.debug("Client created successfully.")
            return response
        except Exception as e:
            logger.error(f"Error creating client: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            logger.debug(f"Client retrieved successfully: {response.data}")
            return response
        except Exception as e:
            logger.error(f"Error retrieving client: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            logger.debug("Client updated successfully.")
            return response
        except Exception as e:
            logger.error(f"Error updating client: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            response = super().destroy(request, *args, **kwargs)
            logger.debug("Client deleted successfully.")
            return response
        except Exception as e:
            logger.error(f"Error deleting client: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClientTitleViewSet(viewsets.ModelViewSet):
    queryset = ClientTitle.objects.all()
    serializer_class = ClientTitleSerializer

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            logger.debug("ClientTitle list retrieved successfully.")
            return response
        except Exception as e:
            logger.error(f"Error retrieving ClientTitle list: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            logger.debug("ClientTitle created successfully.")
            return response
        except Exception as e:
            logger.error(f"Error creating ClientTitle: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            logger.debug(f"ClientTitle retrieved successfully: {response.data}")
            return response
        except Exception as e:
            logger.error(f"Error retrieving ClientTitle: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            logger.debug("ClientTitle updated successfully.")
            return response
        except Exception as e:
            logger.error(f"Error updating ClientTitle: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            response = super().destroy(request, *args, **kwargs)
            logger.debug("ClientTitle deleted successfully.")
            return response
        except Exception as e:
            logger.error(f"Error deleting ClientTitle: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClientTypeViewSet(viewsets.ModelViewSet):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            logger.debug("ClientType list retrieved successfully.")
            return response
        except Exception as e:
            logger.error(f"Error retrieving ClientType list: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            logger.debug("ClientType created successfully.")
            return response
        except Exception as e:
            logger.error(f"Error creating ClientType: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            logger.debug(f"ClientType retrieved successfully: {response.data}")
            return response
        except Exception as e:
            logger.error(f"Error retrieving ClientType: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            logger.debug("ClientType updated successfully.")
            return response
        except Exception as e:
            logger.error(f"Error updating ClientType: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            response = super().destroy(request, *args, **kwargs)
            logger.debug("ClientType deleted successfully.")
            return response
        except Exception as e:
            logger.error(f"Error deleting ClientType: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClientNatureViewSet(viewsets.ModelViewSet):
    queryset = ClientNature.objects.all()
    serializer_class = ClientNatureSerializer

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            logger.debug("ClientNature list retrieved successfully.")
            return response
        except Exception as e:
            logger.error(f"Error retrieving ClientNature list: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            logger.debug("ClientNature created successfully.")
            return response
        except Exception as e:
            logger.error(f"Error creating ClientNature: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            logger.debug(f"ClientNature retrieved successfully: {response.data}")
            return response
        except Exception as e:
            logger.error(f"Error retrieving ClientNature: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            logger.debug("ClientNature updated successfully.")
            return response
        except Exception as e:
            logger.error(f"Error updating ClientNature: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            response = super().destroy(request, *args, **kwargs)
            logger.debug("ClientNature deleted successfully.")
            return response
        except Exception as e:
            logger.error(f"Error deleting ClientNature: {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClientFileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        errors = handle_uploaded_file(file)
        if errors:
            return Response({"status": "partial_success", "errors": errors}, status=status.HTTP_207_MULTI_STATUS)
        return Response({"status": "success"}, status=status.HTTP_201_CREATED)
