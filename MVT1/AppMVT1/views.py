from django.http import HttpResponse
from AppMVT1.models import Familiares
from django.template import loader
from django.shortcuts import render

def listado_familiares(request):
    familiares = Familiares.objects.all()
    diccionario = {"datos": familiares}
    plantilla = loader.get_template("index.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
