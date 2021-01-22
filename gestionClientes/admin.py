
from django.contrib import admin
from gestionClientes.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'DNI',
        'name',
        'email',
        'birth',
        'creation_day',
        'imge',
        'band'
    ) 


admin.site.register(Cliente, ClienteAdmin)
