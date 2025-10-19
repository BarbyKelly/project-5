# Base from Boutique Ado. Edited with ChatGPT to make Home page Products Home page
from django.urls import path
from . import views

urlpatterns = [
    path('', products_views.all_products, name='home')
]
