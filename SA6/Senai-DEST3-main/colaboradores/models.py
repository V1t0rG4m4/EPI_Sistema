from django.db import models


class Colaborador(models.Model):
    nome = models.CharField(max_length=120)
    matricula = models.CharField(max_length=30, unique=True)
    setor = models.CharField(max_length=80)
    cargo = models.CharField(max_length=80)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula}"
