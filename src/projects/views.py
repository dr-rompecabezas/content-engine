from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from .models import Project


def delete_project_from_session(request):
    if "project_slug" in request.session:
        del request.session["project_slug"]
    return redirect("/")


def activate_project_view(request, slug=None):
    try:
        project = Project.objects.get(owner=request.user, slug=slug)
    except Project.DoesNotExist:
        project = None
    if project is None:
        messages.error(request, "Project could not be activated")
        delete_project_from_session(request)
    request.session["project_slug"] = slug
    messages.success(request, "Project activated")
    return redirect("/")


def deactivate_project_view(request, slug=None):
    delete_project_from_session(request)
    return redirect("/")
