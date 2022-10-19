from rest_framework import viewsets
from order.models import Accepted, AcceptedDetail, Dispatch, DispatchDetail, Order, Rejected, RejectedDetail, Sale, SaleDetail

from order.serializers import AcceptedDetailSerializer, AcceptedSerializer, DispatchDetailSerializer, DispatchSerializer, OrderSerializer, RejectedDetailSerializer, RejectedSerializer, SaleDetailSerializer, SaleSerializer

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()

class SaleDetailViewSet(viewsets.ModelViewSet):
    serializer_class = SaleDetailSerializer
    queryset = SaleDetail.objects.all()

class DispatchViewSet(viewsets.ModelViewSet):
    serializer_class = DispatchSerializer
    queryset = Dispatch.objects.all()

class DispatchDetailViewSet(viewsets.ModelViewSet):
    serializer_class = DispatchDetailSerializer
    queryset = DispatchDetail.objects.all()

class AcceptedViewSet(viewsets.ModelViewSet):
    serializer_class = AcceptedSerializer
    queryset = Accepted.objects.all()

class AcceptedDetailViewSet(viewsets.ModelViewSet):
    serializer_class = AcceptedDetailSerializer
    queryset = AcceptedDetail.objects.all()

class RejectedViewSet(viewsets.ModelViewSet):
    serializer_class = RejectedSerializer
    queryset = RejectedDetail.objects.all()

class RejectedDetailViewSet(viewsets.ModelViewSet):
    serializer_class = RejectedDetailSerializer
    queryset = RejectedDetail.objects.all()