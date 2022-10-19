from dataclasses import fields
from rest_framework import serializers

from road.models import Road, RoadCargo, RoadMap

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = ('__all__')

class RoadMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadMap
        fields = ('__all__')

class RoadCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadCargo
        fields = ('__all__')