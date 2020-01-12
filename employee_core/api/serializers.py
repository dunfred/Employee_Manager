from rest_framework import serializers
from employee_core.models import Employee

class EmployeeObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'