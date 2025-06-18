from django.urls import path
from . import views

urlpatterns = [
    path('', views.howto_part, name='howto'),
]
