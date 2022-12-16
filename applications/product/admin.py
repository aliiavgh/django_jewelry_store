from django.contrib import admin

from applications.product.models import Product, Material

admin.site.register(Product)
admin.site.register(Material)