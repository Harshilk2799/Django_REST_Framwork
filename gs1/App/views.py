from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer


# Model Object - (Single record)

# def student_data(request, pk):
#     # stu = Student.objects.get(id = 2)
#     stu = Student.objects.get(id = pk)
#     print("Object: ",stu)
#     serializer = StudentSerializer(stu)
#     print("Serializer: ",serializer)
#     print("Serializer data: ", serializer.data)
#     json_data = JSONRenderer().render(serializer.data)
#     print("Json Data: ", json_data)
#     return HttpResponse(json_data, content_type="application/json")

# Using JsonResponse()
def student_data(request, pk):
    # stu = Student.objects.get(id = 2)
    stu = Student.objects.get(id = pk)
    print("Object: ",stu)
    serializer = StudentSerializer(stu)
    print("Serializer: ",serializer)
    print("Serializer data: ", serializer.data)
    return JsonResponse(serializer.data)


# ======================================================================================


# Queryset  - (All record)

# def student_list(request):
#     # stu = Student.objects.get(id = 2)
#     stu = Student.objects.all()
#     print("Object: ",stu)
#     serializer = StudentSerializer(stu, many=True)
#     print("Serializer: ",serializer)
#     print("Serializer data: ", serializer.data)
#     json_data = JSONRenderer().render(serializer.data)
#     print("Json Data: ", json_data)
#     return HttpResponse(json_data, content_type="application/json")


# Using JsonResponse()
def student_list(request):
    # stu = Student.objects.get(id = 2)
    stu = Student.objects.all()
    print("Object: ",stu)
    serializer = StudentSerializer(stu, many=True)
    print("Serializer: ",serializer)
    print("Serializer data: ", serializer.data)
    return JsonResponse(serializer.data, safe=False)