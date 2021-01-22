from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from gestionClientes.models import *

class ListUsers(ListView):
    model = Cliente
    template_name = 'list.html'
    def get_queryset(self):
        return self.model.objects.all()
    
class Users(TemplateView):
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        self.request = request

        return render(request, self.template_name, {})
