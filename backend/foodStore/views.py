from rest_framework import viewsets
from .serializers import *
from .models import *

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class SideViewSet(viewsets.ModelViewSet):
    queryset = Side.objects.all()
    serializer_class = SideSerializer
    

class FoodOrderViewSet(viewsets.ModelViewSet):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderSerializer