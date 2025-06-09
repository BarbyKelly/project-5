from .models import Recommendation
from django import forms


# Recommendation URLField
recommendation_url = forms.URLField(
    label="Please include URL with your Recommendation",
    widget=forms.URLInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Please add link to your Recommendation'
        }
    )
)
