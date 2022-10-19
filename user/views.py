from rest_framework import viewsets
from user.models import Customer, CustomerCategory, Location, User

from user.serializers import CustomerCategorySerializer, CustomerSerializer, LocationSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class CustomerCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerCategorySerializer
    queryset = CustomerCategory.objects.all()

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()