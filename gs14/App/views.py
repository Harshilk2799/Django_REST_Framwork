from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# ModelViewSet
class StudentModelViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# ReadOnlyModelViewSet
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

