from . import cache as project_cache

from .models import Project


def user_projects_context(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        user_projects = project_cache.get_user_projects(username=username)
        return {'user_projects': user_projects}
    return {'user_projects': Project.objects.none()}
