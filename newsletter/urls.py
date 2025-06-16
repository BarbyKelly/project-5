from django.urls import path
from . import views


urlpatterns = [
    path('newsletter/', views.Newsletter.as_view, name='newsletter'),
]
