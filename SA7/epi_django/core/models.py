from django.db import models


class Colaborador(models.Model):
    nome      = models.CharField('Nome Completo', max_length=200)
    matricula = models.CharField('Matrícula', max_length=50, unique=True)
    cargo     = models.CharField('Cargo', max_length=100)
    setor     = models.CharField('Setor', max_length=100)
    telefone  = models.CharField('Telefone', max_length=20, blank=True)
    email     = models.EmailField('E-mail', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        ordering            = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.matricula})'


class Equipamento(models.Model):
    nome      = models.CharField('Nome do EPI', max_length=200)
    codigo    = models.CharField('Código', max_length=50, unique=True)
    descricao = models.TextField('Descrição', blank=True)
    quantidade= models.PositiveIntegerField('Quantidade', default=1)
    ca        = models.CharField('Certificado de Aprovação (CA)', max_length=50, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
        ordering            = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.codigo})'


class Emprestimo(models.Model):
    STATUS = [
        ('Emprestado', 'Emprestado'),
        ('Fornecido',  'Fornecido'),
        ('Devolvido',  'Devolvido'),
        ('Danificado', 'Danificado'),
        ('Perdido',    'Perdido'),
    ]
    STATUS_CADASTRO  = ['Emprestado', 'Fornecido']
    STATUS_DEVOLUCAO = ['Devolvido', 'Danificado', 'Perdido']

    colaborador             = models.ForeignKey(Colaborador, on_delete=models.PROTECT,
                                                verbose_name='Colaborador')
    equipamento             = models.ForeignKey(Equipamento, on_delete=models.PROTECT,
                                                verbose_name='Equipamento')
    data_emprestimo         = models.DateTimeField('Data de Entrega')
    data_prevista_devolucao = models.DateTimeField('Previsão de Devolução')
    data_devolucao          = models.DateTimeField('Data de Devolução', null=True, blank=True)
    status                  = models.CharField('Status', max_length=20,
                                               choices=STATUS, default='Emprestado')
    observacao_devolucao    = models.TextField('Observação', blank=True)
    criado_em               = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering            = ['-criado_em']

    def __str__(self):
        return f'{self.colaborador.nome} — {self.equipamento.nome} [{self.status}]'
