# Code learned from:
# https://github.com/tmarkec/row_to_grow/blob/main/subscription/apps.py
from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter'
