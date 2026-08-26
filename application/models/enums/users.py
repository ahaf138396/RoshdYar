from enum import Enum

class Users(str, Enum):
    USER_ID = 'user_id'
    USERNAME = 'username'
    EMAIL = 'email'
    PHONE = 'phone_number'
    IS_ACTIVE = 'is_active'
    IS_REMOVED = 'is_removed'

class REMOVED_USERS(str, Enum):
    USER_ID = 'user_id'
    REMOVED_AT = 'removed_at'
    REMOVED_BY = 'removed_by'

class UserStatus(str, Enum):
    ACTIVE = 'active'
    SUSPENDED = 'suspended'
    REMOVED = 'removed'