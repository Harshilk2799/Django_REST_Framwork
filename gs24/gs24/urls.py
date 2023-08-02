from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("studentapi/", views.StudentList.as_view()),
    path("studentapi/search/", views.StudentListSearch.as_view()),
    path("studentapi/order/", views.StudentListOrder.as_view()),
]
