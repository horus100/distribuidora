from rest_framework import serializers
from units.models import Umeasure, Umoney


class UmeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Umeasure
        fields = ('__all__')

class UmonetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Umoney
        fields = ('__all__')