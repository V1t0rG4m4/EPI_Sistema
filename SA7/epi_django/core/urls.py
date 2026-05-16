from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Dashboard
    path('', views.index, name='index'),

    # Colaboradores
    path('colaboradores/',               views.colaboradores_lista,  name='colaboradores_lista'),
    path('colaboradores/novo/',          views.colaboradores_novo,   name='colaboradores_novo'),
    path('colaboradores/<int:pk>/editar/', views.colaboradores_editar, name='colaboradores_editar'),
    path('colaboradores/<int:pk>/excluir/', views.colaboradores_excluir, name='colaboradores_excluir'),

    # Equipamentos
    path('equipamentos/',               views.equipamentos_lista,   name='equipamentos_lista'),
    path('equipamentos/novo/',          views.equipamentos_novo,    name='equipamentos_novo'),
    path('equipamentos/<int:pk>/editar/', views.equipamentos_editar, name='equipamentos_editar'),
    path('equipamentos/<int:pk>/excluir/', views.equipamentos_excluir, name='equipamentos_excluir'),

    # Empréstimos
    path('emprestimos/',                views.emprestimos_lista,    name='emprestimos_lista'),
    path('emprestimos/novo/',           views.emprestimos_novo,     name='emprestimos_novo'),
    path('emprestimos/<int:pk>/editar/', views.emprestimos_editar,  name='emprestimos_editar'),
]
