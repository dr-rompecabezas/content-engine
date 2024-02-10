from django.core.cache import cache

from .models import Project, AnonymousProject


class ProjectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not hasattr(request, "project"):
            request.project = AnonymousProject()
            if request.user.is_authenticated:
                # comes via project activation view
                project_slug = request.session.get("project_slug")
                project = None
                cache_str = None
                if project_slug is not None:
                    cache_str = f"_project_slug_cache_{project_slug}"
                    project = cache.get(cache_str)
                if project is None and project_slug is not None:
                    try:
                        project = Project.objects.get(slug=project_slug)
                    except Project.DoesNotExist:
                        pass
                if project is not None:
                    cache.set(cache_str, project)
                    request.project = project
        return self.get_response(request)
