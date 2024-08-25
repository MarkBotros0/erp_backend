from rest_framework import serializers
from .models import Client, ClientTitle, ClientType, ClientNature

class ClientTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTitle
        fields = '__all__'

class ClientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = '__all__'

class ClientNatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientNature
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    title = ClientTitleSerializer()
    client_type = ClientTypeSerializer()
    client_nature = ClientNatureSerializer()

    class Meta:
        model = Client
        fields = '__all__'
