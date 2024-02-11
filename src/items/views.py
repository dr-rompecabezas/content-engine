from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from projects.decorators import project_required

from .forms import ItemCreateForm, ItemUpdateForm
from .models import Item


@project_required
@login_required
def item_list_view(request):
    items = Item.objects.filter(project=request.project)
    return render(request, "items/list.html", {"items": items})


@project_required
@login_required
def item_detail_view(request, id=None):
    item = get_object_or_404(Item, id=id, project=request.project)
    return render(request, "items/detail.html", {"item": item})


@project_required
@login_required
def item_create_view(request):
    form = ItemCreateForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.project = request.project
        item.created_by = request.user
        item.save()
        return redirect(item.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "items/create.html", context)


@project_required
@login_required
def item_update_view(request, id=None):
    item = get_object_or_404(Item, id=id, project=request.project)
    form = ItemUpdateForm(request.POST or None, instance=item)
    if form.is_valid():
        item = form.save(commit=False)
        item.last_modified_by = request.user
        item.save()
        return redirect(item.get_absolute_url())
    context = {
        "item": item,
        "form": form,
    }
    return render(request, "items/update.html", context)


@project_required
@login_required
def item_delete_view(request, id=None):
    item = get_object_or_404(Item, id=id, project=request.project)
    if request.method == "POST":
        item.delete()
        return redirect("items:list")
    context = {
        "item": item,
    }
    return render(request, "items/delete.html", context)
