from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date',
                       'order_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'order_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)