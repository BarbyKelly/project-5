# Base for contact app and form from Boutique Ado, and
# https://github.com/denisklopotan/vegan-sneaker-store/blob/main/contact/views.py
# Form success fixes learned from Chat GPT, and views.py edited accordingly
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import ContactForm


class Contact(View):
    """
    A view that renders Contact Form
    """
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, 'contact/contact.html',
                      {'contact_form': form, 'submitted': False})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            confirmation_text = (
                'Thank you.'
                ' Your message was submitted.'
                ' We hope to reply within 3 working days.'
            )
            # Clearing form after valid submission
            return render(
                request, 'contact/contact.html',
                {'submitted': True,
                    'confirmation_text': confirmation_text})

        # If form invalid, keep Contact Form open with errors
        return render(request, 'contact/contact.html',
                      {'contact_form': form,  'submitted': False})
