from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def student_crud_api(request, id=None):
    if request.method == "GET":
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        print("Data:", request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Successfully Created!!!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    if request.method == "PUT":
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated Successfully!!!"})
        return Response(serializer.errors)

    if request.method == "PATCH":
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated Partially Successfully!!!"})
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"msg":"Data Deleted!!!"})