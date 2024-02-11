from django.shortcuts import render

from items.models import Item
from projects.decorators import project_required


@project_required
def dashboard(request):
    return render(request, "core/dashboard.html")


def home(request):
    if not request.user.is_authenticated:
        return render(request, "core/home.html")
    return dashboard(request)
