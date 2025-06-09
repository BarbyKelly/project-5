from . import views
from django.urls import path


urlpatterns = [
    path('', views.howto_part, name='howto'),
]
