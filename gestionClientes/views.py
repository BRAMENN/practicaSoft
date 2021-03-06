from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from gestionClientes.models import *
from django.core import serializers
from django.http import HttpResponse
from datetime import datetime

class Users(TemplateView):
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        self.request = request

        return render(request, self.template_name, {})

class crearCliente(TemplateView):
    template_name = 'create.html'

    def get(self, request, *args, **kwargs):
        self.request = request

        return render(request, self.template_name, {})

        
class ListUser(TemplateView):

    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        res = Cliente.objects.filter(   Q(name=busqueda) |
                                        Q(DNI=busqueda) &
                                        Q(band=False))
        data = serializers.serialize('json', res)
        print(res)
        return HttpResponse(data, content_type='application/json')

class eliminarCliente(TemplateView):

    def get(self, request, *args, **kwargs):
        dato = request.GET['pk']
        identificador = Cliente.objects.get(pk=dato)
        identificador.band = True
        identificador.save()
        return HttpResponse()

class guardarCliente(TemplateView):

    def get(self, request, *args, **kwargs):
        name = request.GET['name']
        DNI = request.GET['DNI']
        birth = request.GET['birth']
        email = request.GET['email']
        cliente = Cliente(  DNI = DNI,
                            name = name,
                            email = email,
                            birth = birth,
                            creation_day = datetime.now(),
                            band = False
                            )
        cliente.save()
        return HttpResponse()
