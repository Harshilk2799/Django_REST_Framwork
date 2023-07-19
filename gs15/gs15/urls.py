from django.contrib import admin
from django.urls import path, include
from App import views
from rest_framework.routers import DefaultRouter

# Creating Default Router Object
router = DefaultRouter()

# Register StStudentViewSets with Router
router.register("studentapi", views.StudentModelViewSets, basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)), #The API URLs are now determined automatically by the router.
]
