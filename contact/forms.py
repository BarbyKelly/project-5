# Base for forms.py learned from https://github.com/denisklopotan/vegan-sneaker-store/blob/main/contact/forms.py
from django import forms
from .models import ContactForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('full_name', 'email',
                  'subject', 'message',)

        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }
