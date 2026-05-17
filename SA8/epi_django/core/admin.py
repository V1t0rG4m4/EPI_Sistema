from django.contrib import admin
from .models import Colaborador, Equipamento, Emprestimo


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display   = ('nome', 'matricula', 'cargo', 'setor', 'telefone', 'criado_em')
    search_fields  = ('nome', 'matricula', 'cargo')
    list_filter    = ('setor',)


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'codigo', 'ca', 'quantidade', 'criado_em')
    search_fields = ('nome', 'codigo', 'ca')


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display  = ('colaborador', 'equipamento', 'data_emprestimo',
                     'data_prevista_devolucao', 'data_devolucao', 'status')
    list_filter   = ('status',)
    search_fields = ('colaborador__nome', 'equipamento__nome')
    date_hierarchy = 'data_emprestimo'
