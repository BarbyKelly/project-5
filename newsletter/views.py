# Base learned from:
# https://github.com/tmarkec/row_to_grow/blob/main/subscription/views.py
# Views fixed with ChatGPT's guidance (toast, imports, def, class, feedback)
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import SubscriptionForm
from .models import Subscriber


def newsletter_subscribing(request):
    """
    Handles Subscription form.
    Email sent for demonstration purposes only.
    Subscribers list available only by Admin via Django.
    """
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            # Save Subscriber - fixed with ChatGPT
            subscriber = form.save()
            email = subscriber.email

            # Send Subscription confirmation email - edited with ChatGPT
            send_mail(
                subject="Kelly's Art & Photo Boutique",
                message=(
                    f"Thank you for subscribing, {email}!\n\n"
                    "Next Newsletter: on the 1st of next month.\n\n"
                    "Please feel free to check out our page: "
                    "https://kellys-art-and-photo-boutique-913058c0223e.herokuapp.com/"
                ),
                from_email="2025studentproject@gmail.com",
                recipient_list=[email],
                fail_silently=False,
            )

            # Redirect to Subscription Form Success page - fixed with ChatGPT
            return redirect('subscription_form_success')

    else:
        form = SubscriptionForm()

    return render(
        request, 'newsletter/newsletter.html', {'subscription_form': form})


def subscription_form_success(request):
    """
    Display "Thank you for subscribing" page
    """
    return render(request, 'newsletter/subscription_form_success.html')

# Learned from: https://bastakiss.com/blog/django-6/how-to-add-a-newsletter-app-to-your-django-website-475
# Edited with ChatGPT's guidance


def newsletter_list(request):
    """
    List of Subscribers for Admin use only
    """
    newsletters = Subscriber.objects.all().order_by('email')
    return render(
        request, 'newsletter/newsletter_list.html',
        {'newsletters': newsletters}
    )


def subscription_form_success(request):
    """
    Display 'Subscription Successful' page
    """
    return render(
        request, 'newsletter/subscription_form_success.html'
    )
