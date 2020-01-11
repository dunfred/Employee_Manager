from django.urls import path, include
from . import views

urlpatterns = [
    path('',        views.retrieve_employees, name="read_all_emp"),
    path('create/', views.create_employee, name="create-emp"),
    path('<int:id>/update/', views.update_employee, name="update-emp"),
    path('<int:id>/delete/', views.delete_employee, name="delete-emp"),
    path('test/',        views.test, name="test"),
]