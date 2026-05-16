from django.contrib import admin

from .models import Colaborador


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ("nome", "matricula", "setor", "cargo", "ativo")
    search_fields = ("nome", "matricula", "setor", "cargo")
    list_filter = ("ativo", "setor", "cargo")
