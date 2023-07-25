from django.contrib import admin
from django.urls import path, include
from App import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from App.token import CustomAuthToken
# Creating Default Router Object
router = DefaultRouter()

# Register StStudentViewSets with Router
router.register("studentapi", views.StudentModelViewSets, basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)), #The API URLs are now determined automatically by the router.
    path("auth/", include("rest_framework.urls")),
    # path('gettoken/', obtain_auth_token),
    path('gettoken/', CustomAuthToken.as_view()),
]
