from django.db import models

PROVINCE_CHOICES = (
    ("Alberta", "AB, Alberta"),
    ("British Columbia", "BC, British Columbia"),
    ("Manitoba", "MB, Manitoba"),
    ("New Brunswick", "NB, New Brunswick"),
    ("Newfoundland and Labrador", "NL, Newfoundland and Labrador"),
    ("Nova Scotia", "NS, Nova Scotia"),
    ("Ontario", "ON, Ontario"),
    ("Prince Edward Island", "PE, Prince Edward Island"),
)

EMPLOYEE_TYPE_CHOICES = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)

STATUS_CHOICES = (
    ("Active", "Active"),
    ("Inactive", "Inactive"),
)

# Create your models here.
class Employee(models.Model):
    registration_no     = models.CharField(default = 0, blank=False, null=False, unique=True, max_length = 120)
    first_name          = models.CharField(default = "", blank=False, null=False, max_length = 120)
    last_name           = models.CharField(default = "", blank=False, null=False, max_length = 120)
    employee_type       = models.CharField(choices=EMPLOYEE_TYPE_CHOICES, max_length = 15)
    date_of_birth       = models.DateField()
    date_of_membership  = models.DateField()
    address             = models.CharField(default = "", blank=False, null=False, max_length = 120)
    city                = models.CharField(default = "", blank=False, null=False, max_length = 120)
    province            = models.CharField(choices=PROVINCE_CHOICES, max_length = 120)
    contact_no          = models.CharField(max_length = 15)
    status              = models.CharField(choices=STATUS_CHOICES, max_length = 120)
    email               = models.EmailField(default="", max_length = 120)
    #active              = models.NullBooleanField(default = '', blank=False, null=False)

    def __str__(self):
        return f"{self.registration_no} | {self.first_name}"

        