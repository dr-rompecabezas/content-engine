from django.urls import path

from . import views

app_name = "items"
urlpatterns = [
    path("", views.item_list_view, name="list"),
    path("<int:id>/", views.item_detail_view, name="detail"),
    path("create/", views.item_create_view, name="create"),
    # path("<int:id>/update/", views.item_update_view, name="update"),
    # path("<int:id>/delete/", views.item_delete_view, name="delete"),
]