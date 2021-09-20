from management.models import Customer, Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    responsable_person = EmployeeSerializer
    res_person_name = serializers.CharField(source='responsable_person.name')

    class Meta:
        model = Customer
        fields = "__all__"
