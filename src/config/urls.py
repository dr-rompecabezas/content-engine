from django.contrib import admin
from django.urls import path, include

from core import views as core_views


urlpatterns = [
    path("", core_views.home, name="home"),
    path("items/", include("items.urls")),
    path("projects/", include("projects.urls")),
    path("admin/", admin.site.urls),
]
