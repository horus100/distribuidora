from rest_framework import viewsets
from units.models import Umeasure, Umoney

from units.serializers import UmeasureSerializer, UmonetSerializer

# Create your views here.

class UmeasureViewSet(viewsets.ModelViewSet):
    serializer_class = UmeasureSerializer
    queryset = Umeasure.objects.all()

class UmoneyViewSet(viewsets.ModelViewSet):
    serializer_class = UmonetSerializer
    queryset = Umoney.objects.all()