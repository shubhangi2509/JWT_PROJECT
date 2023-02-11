from django.urls import path

from.views import EmployeeViewSet



urlpatterns = [
    path('emp/',EmployeeViewSet.as_view({'post':'create','get':'list'})),
    path('emp/<int:pk>/',EmployeeViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}))
]