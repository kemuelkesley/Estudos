from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from . models import Evento, Cidade, Bairro, CadastroCliente, Sexo


class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome_evento', 'data_evento',)
    prepopulated_fields = {'slug': ('nome_evento',)}
    search_fields = ['nome_evento', 'data_evento',]

admin.site.register(Evento, EventoAdmin)

class CidadeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cidade, CidadeAdmin)

class BairroAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bairro, BairroAdmin)

class CadastroClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome_completo',
        'email',
        'contato'
    )
    
admin.site.register(CadastroCliente, CadastroClienteAdmin)


class SexoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sexo, SexoAdmin)


