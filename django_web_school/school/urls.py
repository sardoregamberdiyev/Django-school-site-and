from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name='home-eng'),
    path("uz/", uzb, name='uz'),
]
