from django.contrib import admin
from .models import Product, Category


# Code from Code Institute Boutique Ado Walksthrough
class ProductAdmin(admin.ModelAdmin):
    """
    Admin view for Product.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'is_print',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin view for Category.
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
