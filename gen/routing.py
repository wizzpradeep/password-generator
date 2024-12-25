from django.urls import path
from .consumers import Consumer

socket_url = [
    path('ws/pass/', Consumer.as_asgi())
]