from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProductRelation


@receiver(post_save, sender=ProductRelation)
def update_dealer_product(sender, instance, created, **kwargs):
    if created:
        dealer_product = instance.dealer_product
        if dealer_product:
            dealer_product.matched = True
            dealer_product.postponed = False
            dealer_product.save()
