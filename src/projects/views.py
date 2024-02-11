from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from .forms import ProjectCreateForm, ProjectUpdateForm
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
    messages.success(request, f"Project {project.title} activated")
    return redirect(reverse("projects:detail", kwargs={"slug": slug}))


def deactivate_project_view(request):
    delete_project_from_session(request)
    messages.success(request, "Project deactivated")
    return redirect("/")


@login_required
def project_list_view(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, "projects/list.html", {"projects": projects})


@login_required
def project_detail_view(request, slug=None):
    project = get_object_or_404(Project, slug=slug, owner=request.user)
    return render(request, "projects/detail.html", {"project": project})


@login_required
def project_create_view(request):
    if not request.project.is_activated:
        return render(request, "projects/activated.html", {})
    form = ProjectCreateForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.owner = request.user
        project.created_by = request.user
        project.save()
        return redirect(project.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "projects/create.html", context)


@login_required
def project_update_view(request, slug=None):
    project = get_object_or_404(Project, slug=slug)
    form = ProjectUpdateForm(request.POST or None, instance=project)
    if form.is_valid():
        project = form.save(commit=False)
        project.last_modified_by = request.user
        project.save()
        return redirect(project.get_absolute_url())
    context = {
        "project": project,
        "form": form,
    }
    return render(request, "projects/update.html", context)


@login_required
def project_delete_view(request, slug=None):
    project = get_object_or_404(Project, slug=slug, owner=request.user)
    if request.method == "POST":
        if project.items.exists():
            messages.error(request, "Project has items and cannot be deleted")
            return redirect(project.get_absolute_url())
        project.delete()
        return redirect("projects:list")
    context = {
        "project": project,
    }
    return render(request, "projects/delete.html", context)
