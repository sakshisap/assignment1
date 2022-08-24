from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):# here we define serializer   
    Emp_name= serializers.CharField(max_length=20)
    Age= serializers.CharField(max_length=10)  
    Desg= serializers.CharField(max_length=20)

    class Meta:
        model = Employee
        fields = ('__all__')