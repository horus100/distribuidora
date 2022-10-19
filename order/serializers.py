from rest_framework import serializers

from order.models import Accepted, AcceptedDetail, Dispatch, DispatchDetail, Order, Rejected, RejectedDetail, Sale, SaleDetail

class OrderSerializer(serializers.ModelSerializer):
    class Meta():
        model= Order
        fields = ('__all__')

class SaleSerializer(serializers.ModelSerializer):
    class Meta():
        model= Sale
        fields = ('__all__')

class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta():
        model = SaleDetail
        fields = ('__all__')

class DispatchSerializer(serializers.ModelSerializer):
    class Meta():
        model= Dispatch
        fields = ('__all__')

class DispatchDetailSerializer(serializers.ModelSerializer):
    class Meta():
        model = DispatchDetail
        fields = ('__all__')

class AcceptedSerializer(serializers.ModelSerializer):
    class Meta():
        model= Accepted
        fields = ('__all__')

class AcceptedDetailSerializer(serializers.ModelSerializer):
    class Meta():
        model = AcceptedDetail
        fields = ('__all__')

class RejectedSerializer(serializers.ModelSerializer):
    class Meta():
        model= Rejected
        fields = ('__all__')

class RejectedDetailSerializer(serializers.ModelSerializer):
    class Meta():
        model = RejectedDetail
        fields = ('__all__')