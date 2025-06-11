from django.db import models


class ContactForm(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=400, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"Message from {self.full_name}: {self.message}"
