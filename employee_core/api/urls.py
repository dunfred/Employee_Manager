from django.urls import path
from .views import EmployeeObjectView

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("employees/", EmployeeObjectView.as_view(), name="all-employees-api"),
]