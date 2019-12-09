
from django.urls import path
from .views import *


urlpatterns = [
    path('', getProducts),
    path('ups', getPro),
]
