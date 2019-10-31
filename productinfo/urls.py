from django.contrib import admin
from django.urls import path
from .views import productInfo


urlpatterns = [
    path ('productinfo', productInfo),
]