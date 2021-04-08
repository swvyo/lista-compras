from django.shortcuts import render, reverse, get_object_or_404, redirect

from .models import Item
from .forms import ItemForm


def list_items(request):
    lista_items = Item.objects.all()

    return render(request, "item/list.html", context={"lista_items": lista_items})


def add_items(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse("items:items"))

    return render(request, "item/add.html", context={"form": form})


def detail_items(request, item_pk):
    item = get_object_or_404(Item.objects, pk=item_pk)

    return render(request, "item/detail.html", context={"item": item})


def edit_items(request, item_pk):
    item = get_object_or_404(Item.objects, pk=item_pk)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect(reverse("items:items"))

    return render(request, "item/edit.html", context={"item": item, "form": form})


def desativar_items(request, item_pk):
    item = get_object_or_404(Item.objects, pk=item_pk)

    item.delete()
    #item.status = "desativado"
    #item.save()

    return redirect(reverse("items:items"))
