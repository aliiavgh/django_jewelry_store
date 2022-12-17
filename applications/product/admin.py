from django.contrib import admin

from applications.product.models import Product, Material, Image


class ImageAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 10


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    list_display = ['id', 'title', 'total_likes']

    def total_likes(self, obj):
        return obj.likes.filter(like=True).count()


admin.site.register(Product, ProductAdmin)
admin.site.register(Material)
admin.site.register(Image)
