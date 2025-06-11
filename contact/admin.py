from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = ('full_name', 'email',
                       'subject', 'message', 'date',)

    fields = ('full_name', 'email',
              'subject', 'message', 'date',)
    
    list_display = ('full_name', 'email', 'date',)
    
    ordering = ('-date',)


admin.site.register(ContactForm, ContactFormAdmin)
