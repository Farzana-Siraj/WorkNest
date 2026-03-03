from django.urls import path

from .views import FormFieldListCreateView, FormListCreateView, ReorderFieldsView

urlpatterns = [
    path("create/", FormListCreateView.as_view(), name="forms"),
    path(
        "<int:form_id>/fields/", FormFieldListCreateView.as_view(), name="form-fields"
    ),
    path(
        "<int:form_id>/fields/reorder/",
        ReorderFieldsView.as_view(),
        name="reorder-fields",
    ),
]
