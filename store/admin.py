from django.contrib import admin
from .models import Product, Order, OrderItem, Customer, DCode

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

#display order items in admin as a single order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_ordered', 'complete')
    list_filter = ('complete', 'date_ordered')
    inlines = [OrderItemInline]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

class DCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(DCode, DCodeAdmin)