from django import forms
from .models import Employee

EMPLOYEE_TYPE_CHOICES = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)

STATUS_CHOICES = (
    ("Active", "Active"),
    ("Inactive", "Inactive"),
)

class CreateEmployeeModelForm(forms.ModelForm):
    employee_type   = forms.ChoiceField(choices=EMPLOYEE_TYPE_CHOICES,
                                        widget=forms.RadioSelect())
    status   = forms.ChoiceField(choices=STATUS_CHOICES,
                                        widget=forms.RadioSelect())
    date_of_birth = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={'type': 'date',
        }))
    date_of_membership = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={'type': 'date',
        }))    

    class Meta:
        model = Employee
        fields = (
            "registration_no", "first_name", "last_name",
            "date_of_birth","employee_type", "date_of_membership",
            "address", "city", "province", "contact_no", "status", "email",
        )