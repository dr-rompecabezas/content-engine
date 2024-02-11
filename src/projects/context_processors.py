from . import cache as project_cache


def user_projects_context(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        user_projects = project_cache.get_user_projects(username=username)
        return {'user_projects': user_projects}
