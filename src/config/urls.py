from django.contrib import admin
from django.urls import path, include

from landing import views as landing_views


urlpatterns = [
    path("", landing_views.home, name="home"),
    path("items/", include("items.urls")),
    path("projects/", include("projects.urls")),
    path("admin/", admin.site.urls),
]
