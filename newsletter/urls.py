# Base learned from:
# https://github.com/tmarkec/row_to_grow/blob/main/subscription/views.py
# Url patterns fixed with ChatGPT's guidance
from django.urls import path
from . import views


urlpatterns = [
    path('', views.newsletter_subscribing, name='newsletter'),
    path('success/', views.subscription_form_success, name='subscription_form_success'),
]
