from django.urls import path
from . import views


urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('subscriber/', views.SubscriptionForm, name='subscription_form.url'),
]
