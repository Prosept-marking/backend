from dealers.models import DealersProducts


def gather_statistics():
    verified_product_count = DealersProducts.objects.filter(
        matched=True).count()
    postponed_product_count = DealersProducts.objects.filter(
        postponed=True).count()
    unverified_product_count = DealersProducts.objects.filter(
        matched=False,
        postponed=False).count()

    print(verified_product_count)
    print(postponed_product_count)
    print(unverified_product_count)
