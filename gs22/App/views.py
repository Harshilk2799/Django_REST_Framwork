from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttle import JackRateThrottle

class StudentModelViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [AnonRateThrottle, JackRateThrottle]