from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ItemCreateForm
from .models import Item


@login_required
def item_create_view(request):
    if not request.project.is_activated:
        return render(request, "projects/activated.html", {})
    form = ItemCreateForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.project = request.project
        item.created_by = request.user
        item.save()
        form = ItemCreateForm()
    context = {
        "form": form
    }
    return render(request, "items/item_create.html", context)
