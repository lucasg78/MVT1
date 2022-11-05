from pipes import Template
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

def saludo(request):
    hoy = datetime.now().strftime("%d/%m/%Y")
    respuesta = f"Bienvenidos - Hoy es {hoy}"
    return HttpResponse(respuesta)