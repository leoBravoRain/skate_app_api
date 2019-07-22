from rest_framework import serializers
from .models import Place

# Serializer of place
class Place_Serializers(serializers.ModelSerializer):

    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Place
        fields = ('id', 'name')

