from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from . import validators

User = settings.AUTH_USER_MODEL


class AnonymousProject():
    value = None
    is_activated = False


class Project(models.Model):
    title = models.CharField(max_length=255, unique=True, validators=[validators.validate_project_title])
    description = models.TextField(blank=True, validators=[validators.validate_project_description])
    slug = models.SlugField(unique=True, validators=[validators.validate_project_slug])
    owner = models.ForeignKey(User, related_name="projects_owned", null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="projects_created", on_delete=models.SET_NULL, null=True)
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name="projects_modified", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})
    
    def get_activate_url(self):
        return reverse("projects:activate", kwargs={"slug": self.slug})

    @property
    def is_activated(self):
        return True
