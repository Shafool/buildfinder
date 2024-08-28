from django.shortcuts import render
from django.views.generic import TemplateView
TEMPLATE_PATH = 'landing/'

class BaseTemplateView(TemplateView):
    template_name = TEMPLATE_PATH + 'base.html'

class LoginTemplateView(TemplateView):
    template_name = TEMPLATE_PATH + 'login.html'
    
class InicioTemplateView(TemplateView):
    template_name = TEMPLATE_PATH + 'inicio.html'

class ContratistaTemplateView(TemplateView):
    template_name = TEMPLATE_PATH + 'contratista.html'

class SubcontratistaTemplateView(TemplateView):
    template_name = TEMPLATE_PATH + 'subcontratista.html'

class CarritoView(TemplateView):
    template_name = TEMPLATE_PATH + 'carrito.html'

class PasarelaView(TemplateView):
    template_name = TEMPLATE_PATH + 'pasarela.html'