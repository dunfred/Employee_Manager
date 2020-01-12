from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from django.http import JsonResponse
from employee_core.api.serializers import EmployeeObjectSerializer
from employee_core.models import Employee

class EmployeeObjectView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        serializer = EmployeeObjectSerializer(qs, many=True) 

        return Response(data=serializer.data)

