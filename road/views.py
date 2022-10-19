from rest_framework import viewsets
from road.models import Road, RoadCargo, RoadMap

from road.serializers import RoadCargoSerializer, RoadMapSerializer, RoadSerializer

# Create your views here.

class RoadViewSet(viewsets.ModelViewSet):
    serializer_class = RoadSerializer
    queryset = Road.objects.all()

class RoadMapViewSet(viewsets.ModelViewSet):
    serializer_class = RoadMapSerializer
    queryset = RoadMap.objects.all()

class RoadCargoViewSet(viewsets.ModelViewSet):
    serializer_class = RoadCargoSerializer
    queryset = RoadCargo.objects.all()