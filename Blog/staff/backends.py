from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import Permission

class ObjectPermissionBackend(BaseBackend):
    def has_perm(self, user_obj, perm, obj=None):
        if not obj or not perm.startswith('staff.change'):
            return False
        if user_obj == obj.autor:
            return True
        return False
    
    def get_all_permissions(self, user_obj, obj=None):
        if not obj:
            return set()
        if user_obj == obj.autor:
            return {'staff.change_videojuegos', 'staff.can_edit_own_post'}
        return set()
    
    def get_user_permissions(self, user_obj, obj=None):
        return self.get_all_permissions(user_obj, obj=obj)