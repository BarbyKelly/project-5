# Base for contact app and form from Boutique Ado, and https://github.com/denisklopotan/vegan-sneaker-store/blob/main/contact/views.py
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views import View
from .forms import ContactForm
from django.contrib import messages


class Contact(View):
    """
    A view that renders Contact page
    """
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'contact/contact.html',
            {
                'contact_form': ContactForm()
            }
        )

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your message was submitted. \
                    We hope to reply within 3 working days.')

        else:
            contact_form = ContactForm()
        return render(
            request,
            'contact/contact.html',
            {
                'contact_form': ContactForm()
            }
        )
