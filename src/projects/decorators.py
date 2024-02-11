from functools import wraps

from django.shortcuts import render


def project_required(view_func):
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.project.is_activated:
            return render(request, "projects/required.html", {})
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func
