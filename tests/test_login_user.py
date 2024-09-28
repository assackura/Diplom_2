import allure

from data import ResponseMessages
from generators import UserGenerator


class TestLoginUser:

    @allure.title('Тест авторизации пользователя')
    @allure.description('Тест проверяет ответы API на попытку авторизоваться зарегистрированным пользователем')
    def test_login_exist_user(self, user_delete_after_test, users):
        response = users.login_user(user_delete_after_test[1]["email"], user_delete_after_test[1]["password"])

        assert response.status_code == 200 and response.json()["success"]

    @allure.title('Тест авторизации пользователя с некорректным паролем')
    @allure.description('Тест проверяет ответы API на попытку авторизоваться зарегистрированным пользователем, '
                        'с указанием не корректного пароля')
    def test_login_with_incorrect_password(self, user_delete_after_test, users):
        response = users.login_user(user_delete_after_test[1]["email"],
                                    UserGenerator.generate_random_string(self, 10))

        assert (response.status_code == 401 and not response.json()["success"] and
                response.json()["message"] == ResponseMessages.INCORRECT_DATA_AUTH)