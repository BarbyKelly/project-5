from django.contrib import admin
from .models import SubscriptionForm


@admin.register(SubscriptionForm)
class SubscriptionFormAdmin(admin.ModelAdmin):
    list_display = ('title', 'added_on',)
    search_fields = ('title', 'content',)
    list_filter = ('status', 'added_on',)
    ordering = ('title',)
