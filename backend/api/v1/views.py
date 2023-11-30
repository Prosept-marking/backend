from dealers.models import DealersNames, DealersProducts
from owner.models import OwnerProducts
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import (DelearNamesSerializer, DelearProductsSerializer,
                          OwnerProductsSerializer)
from .utils.product_matching import matching


class DealerNamesViewSet(viewsets.ModelViewSet):
    queryset = DealersNames.objects.all()
    serializer_class = DelearNamesSerializer


class DealerProductsViewSet(viewsets.ModelViewSet):
    queryset = DealersProducts.objects.all()
    serializer_class = DelearProductsSerializer


class OwnerProductsViewSet(viewsets.ModelViewSet):
    queryset = OwnerProducts.objects.all()
    serializer_class = OwnerProductsSerializer

    @action(detail=False, methods=['GET'])
    def match_product(self, request):
        dealer_product_id = request.query_params.get('id')
        if dealer_product_id:
            dealer_product = DealersProducts.objects.get(id=dealer_product_id)
            name = dealer_product.product_name
            matched_products = matching(name)
            return Response(matched_products)
        else:
            return Response('No id')
