from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ColaboradorForm
from .models import Colaborador


class ColaboradorListView(ListView):
    model = Colaborador
    template_name = "colaboradores/colaborador_list.html"
    context_object_name = "colaboradores"

    def get_queryset(self):
        queryset = super().get_queryset()
        pesquisa = self.request.GET.get("q", "").strip()
        if pesquisa:
            queryset = queryset.filter(nome__icontains=pesquisa)
        self.pesquisa = pesquisa
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pesquisa"] = getattr(self, "pesquisa", "")
        return context


class ColaboradorCreateView(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = "colaboradores/colaborador_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Colaborador cadastrado com sucesso.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Não foi possível cadastrar o colaborador. Verifique os campos informados.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("colaboradores:cadastrar")


class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    template_name = "colaboradores/colaborador_form.html"
    success_url = reverse_lazy("colaboradores:lista")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Colaborador atualizado com sucesso.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Não foi possível atualizar o colaborador. Verifique os campos informados.")
        return super().form_invalid(form)


class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = "colaboradores/colaborador_confirm_delete.html"
    success_url = reverse_lazy("colaboradores:lista")

    def delete(self, request, *args, **kwargs):
        colaborador = self.get_object()
        messages.success(request, f"Colaborador '{colaborador.nome}' excluído com sucesso.")
        return super().delete(request, *args, **kwargs)
