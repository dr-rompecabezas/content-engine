from django.conf import settings
from django.db import models
from django.urls import reverse

from projects.models import Project

User = settings.AUTH_USER_MODEL


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="items")
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="items_created", on_delete=models.SET_NULL, null=True)
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name="items_modified", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("items:detail", kwargs={"id": self.id})
    