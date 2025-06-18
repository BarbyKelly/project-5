# Base for newsletter app learned from:
# https://github.com/tmarkec/row_to_grow/blob/main/subscription/admin.py
from django.contrib import admin
from .models import Subscriber, Newsletter


class SubscriberAdmin(admin.ModelAdmin):
    """
    Subscribers list
    """
    list_display = ("email", "added_on")

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Newsletter)
