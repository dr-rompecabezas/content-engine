from django import forms

from .models import Project


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description"]


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description"]
