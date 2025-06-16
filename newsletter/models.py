# Base for Newsletter app learned from:
# https://bastakiss.com/blog/django-6/how-to-add-a-newsletter-app-to-your-django-website-475
from django.db import models


class Newsletter(models.Model):
    """
    Model for Newsletter
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class SubscriptionForm(models.Model):
    """
    Model for Newsletter Subscription
    """
    email = models.EmailField(unique=True)
    subscribed_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
