from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Cart

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_image', 'name', 'category', 'price', 'stock', 'is_available', 'created_at')
    list_filter = ('category', 'is_available', 'created_at')
    search_fields = ('name', 'description', 'category')
    list_editable = ('price', 'stock', 'is_available')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10
    
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'price', 'description', 'image')
        }),
        ('Specifications', {
            'fields': ('display_size', 'storage', 'ram', 'battery'),
            'classes': ('collapse',)
        }),
        ('Inventory', {
            'fields': ('stock', 'is_available')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )


    def product_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;">', obj.image.url)
        return "No Image"
    product_image.short_description = 'Image'

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'total_price', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'product__name')
    readonly_fields = ('created_at',)
    list_per_page = 20

    def total_price(self, obj):
        return f"${obj.total_price}"
    total_price.short_description = 'Total Price'
