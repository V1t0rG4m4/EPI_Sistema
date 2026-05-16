from django.urls import path

from .views import ColaboradorCreateView, ColaboradorDeleteView, ColaboradorListView, ColaboradorUpdateView


app_name = "colaboradores"

urlpatterns = [
    path("", ColaboradorListView.as_view(), name="lista"),
    path("colaboradores/novo/", ColaboradorCreateView.as_view(), name="cadastrar"),
    path("colaboradores/<int:pk>/editar/", ColaboradorUpdateView.as_view(), name="editar"),
    path("colaboradores/<int:pk>/excluir/", ColaboradorDeleteView.as_view(), name="excluir"),
]
