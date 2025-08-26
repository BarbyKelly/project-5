# Code for contact/urls.py learned from https://github.com/denisklopotan/vegan-sneaker-store/blob/main/contact/urls.py
from django.urls import path
from .views import Contact

urlpatterns = [
    path('contact/', Contact.as_view(), name='contact'),
]
