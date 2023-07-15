from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("studentapi/", views.StudentCRUDAPI.as_view()),
    path("studentapi/<int:id>/", views.StudentCRUDAPI.as_view())
]
