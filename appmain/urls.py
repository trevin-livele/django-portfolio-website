from django.urls import path,include
from .import views

from django.urls import path
from . import views



urlpatterns = [
    path('services/',views.services, name='services'),
    path('portfolio/',views.portfolio, name='portfolio'),
]
