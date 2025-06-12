# Code for contact/admin.py learned from https://github.com/denisklopotan/vegan-sneaker-store/blob/main/contact/admin.py
from django.contrib import admin
from .models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email',
                    'subject', 'message', 'date',)

    search_fields = ('full_name', 'email',
                     'subject', 'message', 'date',)
    list_filter = ('full_name', 'email', 'date',)
    ordering = ('-date',)
