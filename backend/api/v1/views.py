from dealers.models import DealersNames, DealersProducts
from owner.models import OwnerProducts
from rest_framework import viewsets

from .serializers import (DelearNamesSerializer, DelearProductsSerializer,
                          OwnerProductsSerializer)


class DealerNamesViewSet(viewsets.ModelViewSet):
    queryset = DealersNames.objects.all()
    serializer_class = DelearNamesSerializer


class DealerProductsViewSet(viewsets.ModelViewSet):
    queryset = DealersProducts.objects.all()
    serializer_class = DelearProductsSerializer


class OwnerProductsViewSet(viewsets.ModelViewSet):
    queryset = OwnerProducts.objects.all()
    serializer_class = OwnerProductsSerializer
