# Base for newsletter app learned from:
# https://github.com/tmarkec/row_to_grow/blob/main/subscription/admin.py
from django.contrib import admin
from .models import Subscriber, Newsletter


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    """
    Subscriber
    """
    list_display = ('email', 'added_on',)
    search_fields = ('email',)
    list_filter = ('email',)
    ordering = ('email',)
