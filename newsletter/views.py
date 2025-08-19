# Base learned from:
# https://github.com/tmarkec/row_to_grow/blob/main/subscription/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Subscriber
from .forms import SubscriptionForm
from .models import Newsletter
from django.contrib import messages
from django.core.mail import send_mail


def newsletter(request):
    """
    Function to handle Subscription
    """
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Subscribed to our Boutique's Newsletter!")
            # Get subscribers email address from the form
            email = request.POST.get("email")

            # Subscription email details
            subject = "Kelly's Art & Photo Boutique"
            message = (
                "Thank you for subscribing to Boutique's newsletter,"
                "our latest products and news will be sent by email."
                "Please feel free to check out our page:"
                "https://kellys-art-and-photo-boutique-913058c0223e.herokuapp.com/"
            )
            from_email = "2025studentproject@gmail.com"

            # List of recipients
            recipient_list = [email]

            # Send email
            send_mail(subject,
                      message, from_email, recipient_list, fail_silently=False)
    else:
        form = SubscriptionForm()

    context = {"form": form}
    return render(
        request, 'newsletter/newsletter.html',
        {
         'subscription_form': SubscriptionForm()
        }
    )


class Newsletter(TemplateView):
    """
    Template name
    """
    template_name = 'newsletter/newsletter.html'

# Learned from:
# https://bastakiss.com/blog/django-6/how-to-add-a-newsletter-app-to-your-django-website-475


def newsletter_list(request):
    newsletters = Subscriber.objects.all().order_by('email')
    return render(
        request, 'subscription_form_success.html',
        {'newsletters': newsletters})
