# Dynamic Messages
def MODULE_LIST(module):
    return module + " list."


def MODULE_LIST_ERROR(module):
    return "Error while listing " + module + "."


def MODULE_STORE_SUCCESS(module):
    return module + " has been added successfully !"


def MODULE_EXISTS(module):
    return "The " + module + " already exists"


def MODULE_STORE_ERROR(module):
    return "Error while storing " + module + "."


def MODULE_SHOW_SUCCESS(module):
    return module + " details."


def MODULE_NOT_FOUND(module):
    return "No " + module + " found."


def MODULE_SHOW_ERROR(module):
    return "Error during " + module + " details."


def MODULE_UPDATE_SUCCESS(module):
    return module + " details has been updated successfully!"


def MODULE_UPDATE_ERROR(module):
    return "Error while updating " + module + "."


# All delete(destroy/status change) method messages
def MODULE_STATUS_CHANGE(module, status):
    return module + " has been " + status + " successfully!"


def MODULE_DELETE_ERROR(module):
    return "Error while deleting " + module


def MODULE_PARAM_MISSING(module):
    return module + " Parameter is missing"


def INVALID_INPUT(param):
    return param + " has invalid value."


def INPUT_BETWEEN(module, min, max):
    return "The " + module + " has value between " + min + " and " + max + "."


# file upload
def FILE_TYPE_MISMATCH(module):
    return "The " + module + " must be a valid image file."


def HIGH_FILE_SIZE(module, size):
    return "The " + module + " can not be grater than " + size + " MB."


def MODULE_EXPORT_ERROR(module):
    return "Error while exporting " + module + "."


def OTP_MESSAGE(otp):
    return "Verify your OTP: " + str(otp)


THROTTLE_ERROR_MESSAGE = "You have exceeded maximum request limit! Try again after some time."

CHANGE_PASSWORD_ERROR = "Error during change password."
CHANGE_PASSWORD_SUCCESS = "Your password has been changed successfully."
CHANGE_EMAIL_SUCCESS = "Your email has been changed successfully"
PASSWORD_MISMATCH = "Incorrect old password."
PASSWORD_LENGTH = "Password must be between 6 to 50 chars."

INCORRECT_PASSWORD = "Your Password is incorrect."
INVALID_CREDENTIALS = "Invalid credentials."

USER_UNAUTHORIZED = "You are not authorized."
LOGIN_USER_INACTIVE = "User is not Active"

LOGIN_ERROR = "Error during login."
LOGIN_SUCCESS = "Login Successful! redirecting..."
LOGIN_OTP_SENT = "OTP for login has been sent to your email id"
LOGIN_ACCOUNT_DISABLED = "Your account is disabled by admin. Please contact support to get it enabled."

EMAIL_NOT_VERIFIED = "You have not verified your email yet. We've sent otp on your registered email. Please verify before login."
PHONE_NOT_VERIFIED = "You have not verified your phone yet. We've sent otp on your registered phone number. Please verify before login."
USER_EMAIL_EXISTS = "Email already exists."
USER_PHONE_EXISTS = "User already exists."
USER_NAME_EXISTS = "Username already exists."

VERIFY_EMAIL_SUCCESS = "Your email has been verified."
VERIFY_PHONE_SUCCESS = "Your mobile number has been verified."
SIGN_UP_ERROR = "Error during user sign up."

MOBILE_NOT_VERIFIED = "You have not verified your mobile yet. Please verify before login."
MOBILE_OTP_SENT_SUCCESS = "We've sent OTP on your mobile number. Please verify your mobile number."

VERIFY_OTP_ERROR = "Error during verify OTP."
ALREADY_VERIFIED = "Your account was already verified."
VERIFY_OTP_EXPIRED = "Your OTP has been expired."
VERIFY_OTP_SUCCESS = "OTP has been verified."
VERIFY_OTP_MISMATCH = "You have entered wrong OTP or Invalid User"

FORGOT_PASSWORD_ERROR = "Error while fogetting password"
FORGOT_PASSWORD_SUCCESS = "Reset password OTP has been sent on provided mobile number."

RESET_PASSWORD_ERROR = "Error during reset password."
RESET_PASSWORD_SUCCESS = "Password reset request has been processed successfully."

OTP_SENT_ERROR = "Error during sending an OTP."
OTP_SENT_SUCCESS = "OTP has been sent successfully on your registered email id."
OTP_RESEND_SUCCESS = "OTP has been resent to your email address"

UNKNOWN_ERR = "Oops something went wrong. Please try again after some time."

LOGOUT_ERROR = "Error during logout."
LOGOUT_SUCCESS = "You have been logged out successfully."

# File upload
FILE_UPLOAD_ERROR = "Error during file upload."

# Token Errors
INVALID_TOKEN = "Your access token is invalid or expired."
ACCESS_TOKEN_REQUIRED = "Please provide the access token."


# Invalid JSON
INVALID_JSON = "Invalid JSON. Failed to parse JSON"
UNAUTHORIZED_ACCESS = "You are not allowed for this operation."

NO_RECORDS_FOUND = "No records found for the specified input data."

SERVER_ERROR_MESSAGE = "Server Error."

# Invalid request
INVALID_REQUEST = "Invalid request."
PARAM_MISSING = "Request parameter missing."

INVALID_EMAIL = "The selected email is invalid."
SIGNUP_USER_ERR = "Error during signup."
SIGNUP_USER_SUCCESS = "You have signed up successfully. Please verify your mobile number by entering the otp sent to your phone"

USER_DESTROY_ENABLED = "User status has been enabled successfully."
USER_DESTROY_DISABLED = "User status has been disabled successfully."

MOBILE_NO_EXISTS = "The selected mobile number has already been registered."
EMAIL_EXISTS = "The email has already been taken."
MOBILE_EXISTS = "The mobile number has already been registered with us."
MOBILE_UPDATE_ERROR = "Error during phone number update"
MOBILE_UPDATE_SUCCESS = "Mobile number has been updated successfully."
MOBILE_SAME_UPDATE = "Please select number other than your registered number."

# RECAPTCHCA
CAPTCHA_NOT_VERIFIED = "Invalid captcha string. Please try again."
CAPTCHA_FAILED = "Captcha verification is failed."

NOT_VALID_PARAMS = "Request has not valid parameters"
INVALID_RECAPTCHA = "Invalid reCaptcha!"
NOT_ACCEPTABLE_REQUEST = "Request Not Acceptable"
OTP_SUBJECT = "Verify your mobile number."
