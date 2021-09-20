from management.serializers import CustomerSerializer, EmployeeSerializer
from management.models import Customer, Employee

# Create your views here.
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
