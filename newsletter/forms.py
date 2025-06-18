# Base for Newsletter app learned from:
# https://github.com/tmarkec/row_to_grow/blob/main/subscription/forms.py
# and https://bastakiss.com/blog/django-6/how-to-add-a-newsletter-app-to-your-django-website-475
from django import forms
from .models import Newsletter


class SubscriptionForm(forms.ModelForm):
    """
    Form for Newsletter Subscription
    """

    class Meta:
        model = Newsletter
        fields = ['email']
