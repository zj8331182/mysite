from management.serializers import EmployeeSerializer
from management.models import Employee
from rest_framework import generics

# Create your views here.
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
