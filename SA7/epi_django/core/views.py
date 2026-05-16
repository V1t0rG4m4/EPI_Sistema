from django.shortcuts      import render, redirect, get_object_or_404
from django.contrib        import messages
from django.db.models      import Q
from django.db             import IntegrityError

from .models import Colaborador, Equipamento, Emprestimo
from .forms  import ColaboradorForm, EquipamentoForm, EmprestimoCadastroForm, EmprestimoEditarForm


# ─────────────────────────────────────────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
def index(request):
    stats = {
        'colaboradores': Colaborador.objects.count(),
        'equipamentos':  Equipamento.objects.count(),
        'emprestados':   Emprestimo.objects.filter(status='Emprestado').count(),
        'fornecidos':    Emprestimo.objects.filter(status='Fornecido').count(),
        'devolvidos':    Emprestimo.objects.filter(status='Devolvido').count(),
        'danificados':   Emprestimo.objects.filter(status='Danificado').count(),
    }
    recentes = (Emprestimo.objects
                .select_related('colaborador', 'equipamento')
                .order_by('-criado_em')[:5])
    return render(request, 'core/index.html', {'stats': stats, 'recentes': recentes})


# ─────────────────────────────────────────────────────────────────────────────
# COLABORADORES
# ─────────────────────────────────────────────────────────────────────────────
def colaboradores_lista(request):
    busca = request.GET.get('busca', '').strip()
    qs    = Colaborador.objects.all()
    if busca:
        qs = qs.filter(nome__icontains=busca)
    return render(request, 'core/colaboradores/lista.html',
                  {'colaboradores': qs, 'busca': busca})


def colaboradores_novo(request):
    form = ColaboradorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        try:
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso!')
            form = ColaboradorForm()        # limpa o formulário
        except IntegrityError:
            messages.error(request, 'Matrícula já cadastrada. Utilize outra.')
    return render(request, 'core/colaboradores/form.html',
                  {'form': form, 'titulo': 'Novo Colaborador', 'novo': True})


def colaboradores_editar(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    form        = ColaboradorForm(request.POST or None, instance=colaborador)
    if request.method == 'POST' and form.is_valid():
        try:
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('core:colaboradores_lista')
        except IntegrityError:
            messages.error(request, 'Matrícula já em uso por outro colaborador.')
    return render(request, 'core/colaboradores/form.html',
                  {'form': form, 'titulo': f'Editar: {colaborador.nome}', 'novo': False,
                   'objeto': colaborador})


def colaboradores_excluir(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        messages.success(request, 'Colaborador excluído com sucesso!')
        return redirect('core:colaboradores_lista')
    return render(request, 'core/confirmar_exclusao.html',
                  {'objeto': colaborador,
                   'tipo': 'colaborador',
                   'voltar_url': 'core:colaboradores_lista'})


# ─────────────────────────────────────────────────────────────────────────────
# EQUIPAMENTOS
# ─────────────────────────────────────────────────────────────────────────────
def equipamentos_lista(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'core/equipamentos/lista.html', {'equipamentos': equipamentos})


def equipamentos_novo(request):
    form = EquipamentoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        try:
            form.save()
            messages.success(request, 'Equipamento cadastrado com sucesso!')
            form = EquipamentoForm()
        except IntegrityError:
            messages.error(request, 'Código já cadastrado. Utilize outro.')
    return render(request, 'core/equipamentos/form.html',
                  {'form': form, 'titulo': 'Novo Equipamento', 'novo': True})


def equipamentos_editar(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    form        = EquipamentoForm(request.POST or None, instance=equipamento)
    if request.method == 'POST' and form.is_valid():
        try:
            form.save()
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect('core:equipamentos_lista')
        except IntegrityError:
            messages.error(request, 'Código já em uso por outro equipamento.')
    return render(request, 'core/equipamentos/form.html',
                  {'form': form, 'titulo': f'Editar: {equipamento.nome}', 'novo': False,
                   'objeto': equipamento})


def equipamentos_excluir(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        messages.success(request, 'Equipamento excluído com sucesso!')
        return redirect('core:equipamentos_lista')
    return render(request, 'core/confirmar_exclusao.html',
                  {'objeto': equipamento,
                   'tipo': 'equipamento',
                   'voltar_url': 'core:equipamentos_lista'})


# ─────────────────────────────────────────────────────────────────────────────
# EMPRÉSTIMOS
# ─────────────────────────────────────────────────────────────────────────────
STATUS_TODOS = [s[0] for s in Emprestimo.STATUS]

def emprestimos_lista(request):
    colab_busca  = request.GET.get('colaborador', '').strip()
    equip_busca  = request.GET.get('equipamento', '').strip()
    status_busca = request.GET.get('status', '').strip()

    qs = Emprestimo.objects.select_related('colaborador', 'equipamento').order_by('-criado_em')

    # Filtro AND: todos os campos preenchidos são combinados
    if colab_busca:
        qs = qs.filter(colaborador__nome__icontains=colab_busca)
    if equip_busca:
        qs = qs.filter(equipamento__nome__icontains=equip_busca)
    if status_busca:
        qs = qs.filter(status=status_busca)

    return render(request, 'core/emprestimos/lista.html', {
        'emprestimos':  qs,
        'status_todos': STATUS_TODOS,
        'colab_busca':  colab_busca,
        'equip_busca':  equip_busca,
        'status_busca': status_busca,
    })


def emprestimos_novo(request):
    form = EmprestimoCadastroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Empréstimo registrado com sucesso!')
        form = EmprestimoCadastroForm()
    return render(request, 'core/emprestimos/form.html',
                  {'form': form, 'titulo': 'Novo Empréstimo'})


def emprestimos_editar(request, pk):
    emprestimo = get_object_or_404(
        Emprestimo.objects.select_related('colaborador', 'equipamento'), pk=pk
    )
    form = EmprestimoEditarForm(request.POST or None, instance=emprestimo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Empréstimo atualizado com sucesso!')
        return redirect('core:emprestimos_lista')
    return render(request, 'core/emprestimos/editar.html',
                  {'form': form, 'emp': emprestimo,
                   'status_devolucao': Emprestimo.STATUS_DEVOLUCAO})
