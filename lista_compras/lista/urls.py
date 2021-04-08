from django.urls import path
from .views import list_items, desativar_items, detail_items, edit_items, add_items

app_name = "lista"

urlpatterns = [
    path("", list_items, name="items"),
    path("adicionar/", add_items, name="adicionar"),
    path("<int:item_pk>/", detail_items, name="detalhes"),
    path("<int:item_pk>/editar/", edit_items, name="editar"),
    path("<int:item_pk>/desativar/", desativar_items, name="desativar"),
]
