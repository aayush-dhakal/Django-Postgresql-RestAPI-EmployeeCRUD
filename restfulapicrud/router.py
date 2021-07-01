from employeeapi.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive

# note for update api call put / at end too. eg: http://127.0.0.1:8000/api/employee/2/
