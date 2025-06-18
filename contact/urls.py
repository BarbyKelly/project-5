# Code for contact/urls.py learned from https://github.com/denisklopotan/vegan-sneaker-store/blob/main/contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.Contact.as_view(), name='contact'),
]
