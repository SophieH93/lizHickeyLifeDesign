from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('item_total',)
    

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'purchase_date', 'order_total',)

    fields = ('order_number', 'purchase_date', 'full_name', 'email', 'phone_number',
             'country', 'postcode', 'town_or_city', 'street_address1', 
             'street_address2', 'county',  'order_total') 
             
    list_display = ('order_number', 'purchase_date', 'full_name', 'order_total',)

    ordering = ('-purchase_date',)


admin.site.register(Order, OrderAdmin)