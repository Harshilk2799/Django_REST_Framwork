from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby="user2")
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["name"]
    filterset_fields = ["name", "roll"]

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)


# SearchFilter
class StudentListSearch(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby="user2")
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search_fields = ["name"]
    search_fields = ["name", "city"]
    # search_fields = ["^name"]


# OrderingFilter
class StudentListOrder(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby="user2")
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["name"]
    # ordering_fields = ["name", "city"]
    # ordering_fields = "__all__"