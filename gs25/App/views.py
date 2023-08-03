from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from .custom_pagination import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination

class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = CustomPageNumberPagination
    # pagination_class = CustomLimitOffsetPagination
    pagination_class = CustomCursorPagination