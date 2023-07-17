from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class StudentViewSets(viewsets.ViewSet):
    def list(self, request):
        print("========== List ==========")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        print("========== Retrieve ==========")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk 
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        print("========== Create ==========")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created!!!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request, pk=None):
        print("========== Update ==========")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk 
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=request.data)
            serializer.save()
            return Response({"msg": "Complete Data Updated!!!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        print("========== Partial Update ==========")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk 
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            serializer.save()
            return Response({"msg": "Partial Data Updated!!!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        print("========== List ==========")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk 
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"msg": "Deleted Data!!!"})