from rest_framework import viewsets
from.serializers import EmployeeSerializer
from.models import Employee
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated




class EmployeeViewSet(viewsets.ViewSet):
    serializer_class = EmployeeSerializer
    qureyset = Employee.objects.all()




    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def list(self,request):
        serializer = self.serializer_class(self.qureyset.all(),many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    



    def retrieve(self,request,pk=None):
        obj = get_object_or_404(self.qureyset.all(),pk=pk)
        serializer = self.serializer_class(obj)
        return Response(data=serializer.data,status=status.HTTP_200_OK)



    def update(self,request,pk=None):
        obj = get_object_or_404(self.qureyset.all(),pk=pk)
        serializer = self.serializer_class(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_204_NO_CONTENT)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



    def partial_update(self,request,pk=None):
        obj = get_object_or_404(self.qureyset.all(),pk=pk)
        serializer = self.serializer_class(data=request.data,instance=obj,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


    def destroy(self,request,pk=None):
        obj = get_object_or_404(self.qureyset.all(),pk=pk)
        obj.delete()
        return Response(data=None,status=status.HTTP_204_NO_CONTENT)