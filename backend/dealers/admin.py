from django.contrib import admin
from .models import DealersNames, DealersProducts

admin.site.register(DealersNames)
admin.site.register(DealersProducts)