# Base for Newsletter app learned from:
# https://bastakiss.com/blog/django-6/how-to-add-a-newsletter-app-to-your-django-website-475
# and from:
# https://github.com/tmarkec/row_to_grow/blob/main/subscription/forms.py
from django import forms
from .models import Newsletter


class SubscriptionForm(forms.ModelForm):
    """
    Model for Newsletter Subscription Form
    """

    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Please enter your email',
                'class': 'form-control',
            }),
        }
