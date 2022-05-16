from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth import get_user_model

User = get_user_model()

class IsAuthorAuthentiocation(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
    

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        return obj.user == request.user
