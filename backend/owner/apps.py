from django.apps import AppConfig


class OwnerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'owner'

    def ready(self):
        from django.db.models.signals import post_save, pre_delete
        from django.dispatch import receiver
        from owner.models import ProductRelation

        @receiver(post_save, sender=ProductRelation)
        def update_dealer_product(sender, instance, created, **kwargs):
            if created:
                dealer_product = instance.dealer_product
                if dealer_product:
                    dealer_product.matched = True
                    dealer_product.postponed = False
                    dealer_product.pk_owner_product = instance.owner_product.pk
                    dealer_product.name_1c_owner = \
                        instance.owner_product.name_1c
                    dealer_product.save()

        @receiver(pre_delete, sender=ProductRelation)
        def cleanup_dealer_product_fields(sender, instance, **kwargs):
            dealer_product = instance.dealer_product
            if dealer_product:
                dealer_product.matched = False
                dealer_product.postponed = False
                dealer_product.pk_owner_product = None
                dealer_product.name_1c_owner = None
                dealer_product.save()
        post_save.connect(update_dealer_product, sender=ProductRelation)
        pre_delete.connect(cleanup_dealer_product_fields,
                           sender=ProductRelation)
