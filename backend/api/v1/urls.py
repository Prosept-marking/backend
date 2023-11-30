from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (DealerNamesViewSet, DealerProductsViewSet,
                    OwnerProductsViewSet, ProductRelationViewSet)

app_name = 'api.v1'

router_v1 = DefaultRouter()
router_v1.register('delear-names', DealerNamesViewSet, 'dealernames')
router_v1.register('delear-products', DealerProductsViewSet, 'dealerproducts')
router_v1.register('owner-products', OwnerProductsViewSet, 'ownerproducts')
router_v1.register(
    'product-relation', ProductRelationViewSet, 'productrelation')

urlpatterns = (
    path('', include(router_v1.urls)),
)
