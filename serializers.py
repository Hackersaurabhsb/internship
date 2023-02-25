from rest_framework import serializers
from .models import Client,Work,Artist
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields='__all__'
class ArtistSerializer(serializers.ModelSerializer):
    works=serializers.PrimaryKeyRelatedField(many=True,queryset=Work.objects.all())
    class Meta:
        model=Artist
        fields='__all__'
class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Work
        fields='__all__'
#the serializer define how the django models are  converted to and from JSON formar for REST API
