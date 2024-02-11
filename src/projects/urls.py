from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
    path("", views.project_list_view, name="list"),
    path("create/", views.project_create_view, name="create"),
    path("deactivate/", views.deactivate_project_view, name="deactivate"),
    path("<slug:slug>/", views.project_detail_view, name="detail"),
    path("<slug:slug>/activate/", views.activate_project_view, name="activate"),
    path("<slug:slug>/update/", views.project_update_view, name="update"),
    path("<slug:slug>/delete/", views.project_delete_view, name="delete"),
]
