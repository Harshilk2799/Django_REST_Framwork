from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("studentapi/", views.student_crud_api),
    path("studentapi/<int:id>/", views.student_crud_api),
    path("auth/", include("rest_framework.urls")),
]
