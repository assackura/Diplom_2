import allure

from data import EndPoints
from api_methods.base import Base

class User(Base):

    @allure.step('Создаем нового пользователя {email}')
    def create_new_user(self, email=None, password=None, name=None):
        body_parametrs = {}
        if email != None:
            body_parametrs["email"] = email
        if password != None:
            body_parametrs["password"] = password
        if name != None:
            body_parametrs["name"] = name
        response = self.post_method(EndPoints.CREATE_USER, None, body_parametrs)
        return response

    @allure.step('Удаляем пользователя')
    def delete_user(self, token):
        headers = {
            "Authorization": f"{token}"
        }
        response = self.delete_method(EndPoints.GET_AND_DELETE_USER, headers, None)
        return response

    @allure.step('Авторизуемся под пользователем {email}')
    def login_user(self, email=None, password=None):
        body_parametrs = {}
        if email != None:
            body_parametrs["email"] = email
        if password != None:
            body_parametrs["password"] = password
        response = self.post_method(EndPoints.AUTH_USER, body=body_parametrs)
        return response

    @allure.step('Выход пользователя')
    def logout_user(self, refreshToken=None):
        body_parametrs = {}
        if refreshToken != None:
            body_parametrs["refreshToken"] = '{{' + refreshToken + '}}'
        response = self.post_method(EndPoints.LOGOUT_USER, body=body_parametrs)
        return response

    @allure.step('Получаем данные пользователя')
    def get_user_data(self, token):
        headers = {
            "Authorization": f"{token}"
        }
        response = self.get_method(EndPoints.GET_AND_DELETE_USER, headers)
        return response

    @allure.step('Изменяем данные пользователя {email} {password} {name}')
    def update_user_data(self, token=None, email=None, password=None, name=None):
        body_parametrs = {}
        headers = {
            "Authorization": f"{token}"
        }
        if email != None:
            body_parametrs["email"] = email
        if password != None:
            body_parametrs["password"] = password
        if name != None:
            body_parametrs["name"] = name
        response = self.patch_method(EndPoints.GET_AND_DELETE_USER, headers, body_parametrs)
        return response