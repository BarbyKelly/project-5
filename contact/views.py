# Base for contact app and form from Boutique Ado, and https://github.com/kera-cudmore/seaside-sewing/blob/main/contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from profiles.models import UserProfile

from django.contrib import messages


def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message was submitted. \
                             We hope to reply within 3 working days.')
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'An error submitting your message. \
                           Please check all required fields, and \
                           try to submit again.')

    else:
        if request.user.is_authenticated:
            try:
                user = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'full_name': user.default_full_name,
                    'email': user.user.email,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': contact_form,
    }

    return render(request, template, context)
