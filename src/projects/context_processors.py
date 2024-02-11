from django.core.cache import cache
from .models import Project


def user_projects_context(request):
    if request.user.is_authenticated:
        cache_str = f"_user_projects_cache_{request.user.username}"
        user_projects = cache.get(cache_str)
        if user_projects is None:
            user_projects = Project.objects.filter(owner=request.user)
            cache.set(cache_str, user_projects)
        return {'user_projects': user_projects}
    return Project.objects.none()
