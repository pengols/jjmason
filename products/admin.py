from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'isbn',
        'category',
        'name',
        'original_author',
        'illustrator',
        'price',
        'publication_year',
        'publisher',
    )

    ordering = ('isbn',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
