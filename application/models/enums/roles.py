from enum import Enum

class RoleType(str, Enum):
    ADMIN = 'admin'
    STAFF = 'staff'
    USER = 'user'
    SUPERUSER = 'superuser'
    CUSTOM_ROLE = 'custom_role'


class RoleColumns(str, Enum):
    ROLE_ID = 'role_id'