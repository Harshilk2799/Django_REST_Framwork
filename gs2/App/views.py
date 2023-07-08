from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io 

# @csrf_exempt
# def student_create(request):
#     if request.method == "POST":
#         json_data = request.body
#         print("Json Data: ", json_data)
#         stream = io.BytesIO(json_data)
#         print("Stream: ", stream)
#         pythondata = JSONParser().parse(stream)
#         print("Python data: ", pythondata)
#         serializer = StudentSerializer(data=pythondata)
#         print("Serializer data: ",serializer)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg": "Data Successfully Created!!!"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type="application/json")
        
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type="application/json")


# Using JsonResponse

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        print("Json Data: ", json_data)
        stream = io.BytesIO(json_data)
        print("Stream: ", stream)
        pythondata = JSONParser().parse(stream)
        print("Python data: ", pythondata)
        serializer = StudentSerializer(data=pythondata)
        print("Serializer data: ",serializer)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "Data Successfully Created!!!"}
            return JsonResponse(res)
        
        return JsonResponse(serializer.errors)