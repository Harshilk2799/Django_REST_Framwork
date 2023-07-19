from rest_framework.permissions import BasePermission
from rest_framework import permissions

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        # 1. Way
        if request.method == "GET":
            return True
        return False


        # 2. Way
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # else:
        #     return False 