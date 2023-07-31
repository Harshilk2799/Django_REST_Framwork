from django.contrib import admin
from django.urls import path, include
from App import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Creating Default Router Object
router = DefaultRouter()

# Register StStudentViewSets with Router
router.register("studentapi", views.StudentModelViewSets, basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)), #The API URLs are now determined automatically by the router.
    path("auth/", include("rest_framework.urls")),
    path("gettoken/", TokenObtainPairView.as_view(), name="Get Token"),
    path("refreshtoken/", TokenRefreshView.as_view(), name="Refresh Token"),
    path("verifytoken/", TokenVerifyView.as_view(), name="Verify Token"),
]
