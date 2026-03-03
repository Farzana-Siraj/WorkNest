from django.urls import path

from .views import EmployeeDeleteView, EmployeeListCreateView

urlpatterns = [
    path("", EmployeeListCreateView.as_view(), name="employees"),
    path("<int:pk>/", EmployeeDeleteView.as_view(), name="employee-delete"),
]
