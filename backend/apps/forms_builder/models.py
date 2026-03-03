from apps.common.models import BaseModel
from django.contrib.auth.models import User
from django.db import models


class Form(BaseModel):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FormField(BaseModel):

    FIELD_TYPES = [
        ("text", "Text"),
        ("number", "Number"),
        ("date", "Date"),
        ("password", "Password"),
        ("email", "Email"),
    ]

    form = models.ForeignKey(Form, related_name="fields", on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)
    required = models.BooleanField(default=True)
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.label} ({self.field_type})"
