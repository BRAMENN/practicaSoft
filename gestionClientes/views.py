from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from gestionClientes.models import *
from django.core import serializers
from django.http import HttpResponse

class Users(TemplateView):
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        self.request = request

        return render(request, self.template_name, {})

class ListUser(TemplateView):

    def get(self, request, *args, **kwargs):
        busqueda = request.GET['busqueda']
        res = Cliente.objects.all()
        data = serializers.serialize('json', res)

        return HttpResponse(data, content_type='application/json')

