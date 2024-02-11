from django.core.exceptions import ValidationError

def validate_project_title(value):
    if len(value) < 3:
        raise ValidationError("Title must be at least 3 characters long")
    if (value).strip().lower() == "create":
        raise ValidationError("The project title may not be 'create'")


def validate_project_description(value):
    if len(value) < 10:
        raise ValidationError("Description must be at least 10 characters long")


def validate_project_slug(value):
    if value.lower() == "create":
        raise ValidationError("Slug may not be 'create'")