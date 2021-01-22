"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionClientes.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route = 'list/',
        view = Users.as_view(),
        name = 'listar_usuarios'
    ),
    path(
        route = 'create/',
        view = crearCliente.as_view(),
        name = 'crear_cliente'
    ),
    path(
        route = 'listClients/',
        view = ListUser.as_view(),
        name = 'listar_clientes'
    ),
    path(
        route = 'eliminarView/',
        view = eliminarCliente.as_view(),
        name = 'eliminar_cliente'
    ),
    path(
        route = 'guardarView/',
        view = guardarCliente.as_view(),
        name = 'eliminar_cliente'
    ),
]
