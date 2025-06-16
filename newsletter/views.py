from django.views import View
from .forms import SubscriptionForm
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse, HttpResponse


class Newsletter(View):
    """
    A view that renders Newsletter's page,
    and sends a confirmation email
    """
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'newsletter/newsletter.html',
            {
                'subscription_form': SubscriptionForm()
            }
        )

    def post(self, request, *args, **kwargs):
        subscription_form = SubscriptionForm(data=request.POST)

        if subscription_form.is_valid():
            subscription_form.save()
            messages.add_message(
                request,
                message.SUCCESS,
                'Your Subscription form was submitted!')

            email = request.POST.get("email")
            title = "Kelly's Art & Photo Boutique's Subscription"
            message = (
                "Thank you for subscribing to our Boutique's newsletter!\n"
                "Feel free to check out our art and photos:\n"
                "https://kellys-art-and-photo-boutique-913058c0223e.herokuapp.com/"
                )
            from_email = "2025studentproject@gmail.com"
            recipient_list = [email]

            send_mail(
                title, message, from_email,
                recipient_list, fail_silently=False)

            return redirect('home')
        else:
            form = SubscriptionForm()

        return render(request, 'newsletter/newsletter.html', {'form': form})


class NewsletterListView(View):
    """
    A view displaying list of Newsletters
    """

    def get(self, request):
        newsletters = Newsletter.objects.all().order_by('created_on')
        return render(
            request, 'newsletter/newsletter_list.html',
            {'newsletters': newsletters})
