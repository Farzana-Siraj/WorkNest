from django.urls import path

from .views import FormListCreateView

urlpatterns = [
    path("create/", FormListCreateView.as_view(), name="forms"),
]
