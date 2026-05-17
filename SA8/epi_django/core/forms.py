from django import forms
from django.utils import timezone
from .models import Colaborador, Equipamento, Emprestimo


# ─── Widget reutilizável ──────────────────────────────────────────────────────
INPUT   = {'class': 'form-control form-control-custom'}
SELECT  = {'class': 'form-select form-control-custom'}
TEXTAREA= {'class': 'form-control form-control-custom', 'rows': 3}
DT_INPUT= {'class': 'form-control form-control-custom', 'type': 'datetime-local'}


# ─── Colaborador ─────────────────────────────────────────────────────────────
class ColaboradorForm(forms.ModelForm):
    class Meta:
        model  = Colaborador
        fields = ['nome', 'matricula', 'cargo', 'setor', 'telefone', 'email']
        widgets = {
            'nome':      forms.TextInput(attrs={**INPUT, 'placeholder': 'Ex.: João da Silva'}),
            'matricula': forms.TextInput(attrs={**INPUT, 'placeholder': 'Ex.: CC-0001'}),
            'cargo':     forms.TextInput(attrs={**INPUT, 'placeholder': 'Ex.: Pedreiro, Eletricista…'}),
            'setor':     forms.TextInput(attrs={**INPUT, 'placeholder': 'Ex.: Estrutural, Elétrico…'}),
            'telefone':  forms.TextInput(attrs={**INPUT, 'placeholder': '(71) 9 0000-0000'}),
            'email':     forms.EmailInput(attrs={**INPUT, 'placeholder': 'colaborador@empresa.com.br'}),
        }


# ─── Equipamento ─────────────────────────────────────────────────────────────
class EquipamentoForm(forms.ModelForm):
    class Meta:
        model  = Equipamento
        fields = ['nome', 'codigo', 'ca', 'quantidade', 'descricao']
        widgets = {
            'nome':      forms.TextInput(attrs={**INPUT, 'placeholder': 'Ex.: Capacete de Segurança'}),
            'codigo':    forms.TextInput(attrs={**INPUT, 'placeholder': 'Ex.: EPI-001'}),
            'ca':        forms.TextInput(attrs={**INPUT, 'placeholder': 'Ex.: 12345'}),
            'quantidade':forms.NumberInput(attrs={**INPUT, 'min': 0}),
            'descricao': forms.Textarea(attrs={**TEXTAREA,
                                               'placeholder': 'Descreva o equipamento, especificações técnicas…'}),
        }


# ─── Empréstimo — cadastro ────────────────────────────────────────────────────
class EmprestimoCadastroForm(forms.ModelForm):
    """Formulário de CADASTRO: status limitado a Emprestado / Fornecido."""

    STATUS_CADASTRO = [('Emprestado', 'Emprestado'), ('Fornecido', 'Fornecido')]

    status = forms.ChoiceField(
        choices=STATUS_CADASTRO,
        widget=forms.Select(attrs=SELECT),
        label='Status',
    )

    class Meta:
        model  = Emprestimo
        fields = ['colaborador', 'equipamento', 'data_emprestimo',
                  'data_prevista_devolucao', 'status']
        widgets = {
            'colaborador':             forms.Select(attrs=SELECT),
            'equipamento':             forms.Select(attrs=SELECT),
            'data_emprestimo':         forms.DateTimeInput(attrs=DT_INPUT, format='%Y-%m-%dT%H:%M'),
            'data_prevista_devolucao': forms.DateTimeInput(attrs=DT_INPUT, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordena os selects
        self.fields['colaborador'].queryset = Colaborador.objects.order_by('nome')
        self.fields['equipamento'].queryset = Equipamento.objects.order_by('nome')
        self.fields['colaborador'].empty_label = '— Selecione o colaborador —'
        self.fields['equipamento'].empty_label = '— Selecione o equipamento —'

    def clean(self):
        """
        Regras de negócio para as datas do empréstimo:
        1. A data prevista para devolução deve ser posterior ao momento atual.
        2. A data prevista para devolução deve ser posterior à data de entrega.
        """
        cleaned = super().clean()
        data_emp   = cleaned.get('data_emprestimo')
        data_prev  = cleaned.get('data_prevista_devolucao')
        agora      = timezone.now()

        if data_prev:
            # Regra 1 — deve ser posterior ao momento atual
            if data_prev <= agora:
                self.add_error(
                    'data_prevista_devolucao',
                    'A data prevista para devolução deve ser posterior à data e hora atuais.'
                )
            # Regra 2 — deve ser posterior à data de entrega
            elif data_emp and data_prev <= data_emp:
                self.add_error(
                    'data_prevista_devolucao',
                    'A data prevista para devolução deve ser posterior à data de entrega.'
                )

        return cleaned


# ─── Empréstimo — edição de status ───────────────────────────────────────────
class EmprestimoEditarForm(forms.ModelForm):
    """Formulário de EDIÇÃO: todos os status disponíveis + campos de devolução."""

    class Meta:
        model  = Emprestimo
        fields = ['status', 'data_devolucao', 'observacao_devolucao']
        widgets = {
            'status':                forms.Select(attrs=SELECT),
            'data_devolucao':        forms.DateTimeInput(attrs=DT_INPUT, format='%Y-%m-%dT%H:%M'),
            'observacao_devolucao':  forms.Textarea(attrs={**TEXTAREA,
                                                           'placeholder': 'Condições de devolução, danos, motivo do extravio…'}),
        }
