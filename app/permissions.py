from rest_framework import permissions


class OwnProfilePermission(permissions.BasePermission):
    message = 'This action is restricted for the owner of this registry or admin users '

    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_superuser

    def has_permission(self, request, obj):
        return request.user and request.user.is_authenticated

class PermissionsPerMethodMixin(object):
    def get_permissions(self):
        """
        Allows overriding default permissions with @permission_classes
        """
        view = getattr(self, self.action)
        if hasattr(view, 'permission_classes'):
            return [permission_class() for permission_class in view.permission_classes]
        return super().get_permissions()