from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_date
from django.http import JsonResponse
from .models import Employee
from .forms import CreateEmployeeModelForm

# Create your views here.

# Create
def create_employee(request):
    form = CreateEmployeeModelForm()
    template = "create.html"
    
    context = {
        "form" : form,
    }
    if request.method == "POST":
        form = CreateEmployeeModelForm(request.POST)
        if form.is_valid:
            new_object = Employee.objects.create(
                registration_no     = form.data.get("registration_no"),
                first_name          = form.data.get("first_name"),
                last_name           = form.data.get("last_name"),
                employee_type       = form.data.get("employee_type"),
                date_of_birth       = parse_date(form.data.get("date_of_birth")),
                date_of_membership  = parse_date(form.data.get("date_of_membership")),
                address             = form.data.get("address"),
                city                = form.data.get("city"),
                province            = form.data.get("province"),
                contact_no          = form.data.get("contact_no"),
                status              = form.data.get("status"),
                email               = form.data.get("email"),
            )
            new_object.save()
            form = CreateEmployeeModelForm()
            return redirect("read_all_emp")
    return render(request, template, context)

# Retrieve
def retrieve_employees(request):
    employees_obj = Employee.objects.all()
    form = CreateEmployeeModelForm()
    template = "read.html"    
        
    context = {
        "employees" : employees_obj,
        "form"      : form,
    }

    return render(request, template, context)

# Update
def update_employee(request, id):    
    template = "update.html"
        
    employee_obj = get_object_or_404(Employee,id=id)

    form = CreateEmployeeModelForm(request.POST or None, instance=employee_obj)
    
    context = {
        "form" : form,
    }
        
    if request.method == "POST":        
        form = CreateEmployeeModelForm(request.POST or None, instance=employee_obj)
        if form.is_valid:
            form.save()

            form = CreateEmployeeModelForm()
            return redirect("read_all_emp")    

    return render(request, template, context)

# Delete
def delete_employee(request, id):        
    employee_obj = get_object_or_404(Employee,id=id)

    data = {
        "message" : f"{employee_obj.first_name} could not be deleted"
    }

    if request.method == "POST":
        #Uncomment below code to allow employee object to be deleted from db

        #employee_obj.delete()
        data["message"] = f"Employee {employee_obj.first_name} deleted successfully."

    return JsonResponse(data)
# testing
def test(request):
    template = "book_list.html"
    
    return render(request, template, {})
