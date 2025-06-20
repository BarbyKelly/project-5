# Base for Newsletter app learned from:
# https://bastakiss.com/blog/django-6/how-to-add-a-newsletter-app-to-your-django-website-475
# and https://github.com/tmarkec/row_to_grow/blob/main/subscription/models.py
from django.db import models


class Newsletter(models.Model):
    """
    Model for Newsletter
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    email = models.EmailField(
        max_length=100, null=False, blank=False)
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    added_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email
