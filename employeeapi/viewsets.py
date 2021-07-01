from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()  # assigned all the retrieved Employee record in querset
    serializer_class = serializers.EmployeeSerializer  # signifies that we should use EmployeeSerializer for json conversion for EmployeeViewSet

# this viewset class basically creates useful api methods like list(), retrieve(), create(), update(), destroy() for convinence