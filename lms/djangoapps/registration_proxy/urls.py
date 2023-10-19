from django.urls import path
from .views import registration_proxy

urlpatterns = [
    path('register-proxy/', registration_proxy, name='register_proxy'),
]
