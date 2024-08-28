from django.contrib import admin
from django.urls import include, path

from apps.landing.views import *

urlpatterns = [
    path("", InicioTemplateView.as_view(), name="inicio"),
    path("login/", LoginTemplateView.as_view(), name="login"),
    path("contratista/", ContratistaTemplateView.as_view(), name="contratista"),
    path("subcontratista/", SubcontratistaTemplateView.as_view(), name="subcontratista"),
    path("carrito/", CarritoView.as_view(), name="carrito"),
    path("pasarela/", PasarelaView.as_view(), name="pasarela"),
]







