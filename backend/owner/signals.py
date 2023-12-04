from dealers.models import DealersProducts
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProductRelation


@receiver(post_save, sender=ProductRelation)
def update_dealer_product(sender, instance, created, **kwargs):
    if created:
        dealer_product_id = instance.dealer_product_id
        if dealer_product_id:
            dealer_product = DealersProducts.objects.filter(
                pk=dealer_product_id
            ).first()
            if dealer_product:
                dealer_product.matched = True
                dealer_product.postponed = False
                dealer_product.save()
