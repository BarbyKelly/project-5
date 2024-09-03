# Code followed from Boutique Ado walk-through, like the rest of the code. Link in README
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
