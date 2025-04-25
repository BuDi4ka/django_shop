from django.contrib import admin
from .models import Product, ProductCategory, Basket

# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    field = ('name', 'description', ('price', 'quantity'), 'category', 'image')
    readonly_fields = ('desription',)
    search_fields = ('name',)
    ordering = ('-name', )


class BasketAdmin(admin.TabularInline):
    model = Basket
    field = ('product', 'quantity')
    extra = 0