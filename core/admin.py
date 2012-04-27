from django.contrib import admin

from core.models import Caminhao, Cliente, Fornecedor, Nota, Transportadora

admin.site.register(Caminhao)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Nota)
admin.site.register(Transportadora)
