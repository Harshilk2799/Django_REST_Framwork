from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("studentapi/", views.StudentListCreateAPI.as_view()),
    path("studentapi/<int:pk>", views.StudentRetrieveUpdateDestroyAPI.as_view()),
]
