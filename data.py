class Urls:
    MAIN_URL = "https://stellarburgers.nomoreparties.site/"

class EndPoints:
    ORDER_BURGER = "api/orders" #POST
    CREATE_USER = "api/auth/register" #POST
    AUTH_USER = "api/auth/login" #POST
    LOGOUT_USER = "api/auth/logout" #POST
    GET_AND_DELETE_USER = "api/auth/user" #GET, DELETE, PATCH
    GET_DATA_ING = "api/ingredients"
    GET_AND_CREATE_NEW_ORDER = "api/orders"

class ResponseMessages:

    USER_EXIST = "User already exists"
    CREATE_USER_WITHOUT_FIELD = "Email, password and name are required fields"
    INCORRECT_DATA_AUTH = "email or password are incorrect"
    CREATE_ORDER_WITHOUT_ING = "Ingredient ids must be provided"
    UPDATE_USER_DATA_WITHOUT_AUTH = "You should be authorised"