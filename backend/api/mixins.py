from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permissions_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
