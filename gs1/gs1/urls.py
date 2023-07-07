from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_info/<int:pk>', views.student_data),
    path('student_info/', views.student_list),
]
