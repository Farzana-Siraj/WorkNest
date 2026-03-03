from django.urls import path

from .views import FormFieldListCreateView, FormListCreateView

urlpatterns = [
    path("create/", FormListCreateView.as_view(), name="forms"),
    path(
        "<int:form_id>/fields/", FormFieldListCreateView.as_view(), name="form-fields"
    ),
]
