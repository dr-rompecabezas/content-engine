from django.shortcuts import render, redirect


def activate_project_view(request, slug=None):
    print(slug)
    return redirect("/")


def deactivate_project_view(request, slug=None):
    return redirect("/")
