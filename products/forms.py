# Base code from Boutique Ado
# Code for fields learned from chatGPT
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from django.forms import Field

class ProductForm(forms.ModelForm):

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            # Default class for all fields
            field.widget.attrs['class'] = 'border-black rounded-0'

        # Make 'Author' field smaller
        if 'author' in self.fields:
            self.fields['author'].widget.attrs['class'] += ' author_field'
        
        # Make 'Description' field smaller
        if 'description' in self.fields:
            self.fields['description'].widget.attrs['class'] += ' description-field'
