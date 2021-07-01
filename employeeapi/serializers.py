from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # this takes in all the columns of the table
        # if you want only some specific columns then define then inside brackets like-> fields = ('id','fullname')