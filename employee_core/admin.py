from django.contrib import admin
from . import models

class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Personal Information", {"fields": ['first_name', 'last_name', 'date_of_birth', 'contact_no','email', 'city', 'address', 'province']}),
        ("Public Information",   {"fields": ['registration_no', 'employee_type', 'date_of_membership', 'status']}),
    )

    radio_fields = {
        "status" : admin.HORIZONTAL,
        "province" : admin.VERTICAL,
        "employee_type" : admin.HORIZONTAL,
    }

# Register your models here.
admin.site.register(models.Employee, EmployeeAdmin)
