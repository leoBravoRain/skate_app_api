from rest_framework import serializers
from .models import Place, Location, Videos_Location

# Serializer of place
class Place_Serializers(serializers.ModelSerializer):

    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Place
        fields = ('id', 'name')


# Serializer of location
class LocationSerializers(serializers.ModelSerializer):

    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Location
        fields = ('id', 'name', 'latitude', 'longitude', 'place')


# Serializer of videos
class Videos_Location_Serializers(serializers.ModelSerializer):

    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Videos_Location
        # fields = ('id', "location","link")
        fields = '__all__'




