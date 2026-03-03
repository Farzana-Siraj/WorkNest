from apps.forms_builder.models import Form
from django.contrib.auth.models import User
from django.db import models


class EmployeeData(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return f"Employee {self.id}"
