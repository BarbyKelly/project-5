# Base for Newsletter app learned from:
# https://github.com/tmarkec/row_to_grow/blob/main/subscription/forms.py
# and https://bastakiss.com/blog/django-6/how-to-add-a-newsletter-app-to-your-django-website-475
# Fixed with ChatGPT, as subscribers only shown in the terminal, and not in Django Admin
from django import forms
from .models import Subscriber


class SubscriptionForm(forms.ModelForm):
    """
    Form for Newsletter Subscription
    """

    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': True
            })
        }
