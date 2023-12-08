from dealers.models import DealersProducts

from .models import OwnerProducts, ProductRelation


def create_relation(dealer_product_id, owner_product_id):
    """Создать сопоставление между товарами по их ID."""
    dealer_product = DealersProducts.objects.get(id=dealer_product_id)
    owner_product = OwnerProducts.objects.get(id=owner_product_id)
    return ProductRelation.objects.create(
        dealer_product=dealer_product,
        owner_product=owner_product,
        matched=True
    )


def cancel_relation(self):
    """Отменить сопоставление."""
    self.matched = False
    self.save()
