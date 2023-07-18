from django.contrib import admin

from webapp.models import Product, Category, Order

admin.site.register(Category)
admin.site.register(Order)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "balance", 'category', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    fields = ['title', 'description', 'price', 'image',
              'created_at', 'category', 'balance']
    readonly_fields = ['created_at']


admin.site.register(Product, ProductAdmin)
# Register your models here.


