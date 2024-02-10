from django.shortcuts import render


def home(request):
    print(request.session.get("project_slug"))
    print(request.project)
    return render(request, "landing/home.html")
