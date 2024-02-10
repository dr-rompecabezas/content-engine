from django.contrib import admin
from django.urls import path, include

from landing import views as landing_views
from projects import views as project_views


urlpatterns = [
    path("", landing_views.home, name="home"),
    path("items/", include("items.urls")),
    path("activate/project/<slug:slug>/", project_views.activate_project_view, name="activate_project"),
    path("deactivate/project/<slug:slug>/", project_views.deactivate_project_view, name="deactivate_project"),
    path("admin/", admin.site.urls),
]
