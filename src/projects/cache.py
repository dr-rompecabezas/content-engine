from django.core.cache import cache as dj_cache

from .models import Project


def get_user_projects(username=None, limit=5, set_on_none=True):
    if username is not None:
        cache_str = f"_user_projects_cache_{username}"
        user_projects = dj_cache.get(cache_str)
        if user_projects is None and set_on_none:
            user_projects = Project.objects.filter(
                owner__username=username
            ).order_by('-modified')[:limit]
            dj_cache.set(cache_str, user_projects)
        return user_projects
    return Project.objects.none()
