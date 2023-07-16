from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# 1. ListAPIView
class StudentListCreate(ListAPIView, CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# 8. RetrieveUpdateDestroyAPIView
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer