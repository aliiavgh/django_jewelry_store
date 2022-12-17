from django.contrib import admin

from applications.product.models import Product, Material, Image

admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Image)