from enum import Enum

class VerificationType(str, Enum):
    PHONE = 'phone'
    EMAIL = 'email'
    PASSWORD_RESET = 'password_reset'

class CredentialType(str, Enum):
    PASSWORD = 'password'
    OTP = 'otp'
    EMAIL = 'email'
    PHONE = 'phone'

