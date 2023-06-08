from django.urls import path
from .views import EmployeeDetil, EmployeeInfo

urlpatterns = [
    path('emp/', EmployeeDetil.as_view(), name='emp'),
    path('emp/<int:id>/', EmployeeInfo.as_view())

]
