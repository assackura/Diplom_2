import allure

from data import ResponseMessages
from generators import UserGenerator


class TestCreateUser:

    @allure.title('Тест создания нового пользователя')
    @allure.description('Тест проверяет ответы API на попытку создать нового, уникального пользователя')
    def test_create_new_unique_user(self, user_delete_after_test):
        assert user_delete_after_test[0].status_code == 200 and user_delete_after_test[0].json()["success"]

    @allure.title('Тест создания нового пользователя без пароля')
    @allure.description('Тест проверяет ответы API на попытку создать нового, уникального пользователя, без '
                        'указания обязательного поля password')
    def test_create_new_user_with_out_password(self, new_user_data, users):
        response = users.create_new_user(email=new_user_data["email"], name=new_user_data["name"])

        assert (response.status_code == 403 and not response.json()["success"] and
                response.json()["message"] == ResponseMessages.CREATE_USER_WITHOUT_FIELD)

    @allure.title('Тест создания существующего пользователя')
    @allure.description('Тест проверяет ответы API на попытку создать пользователя, который уже зарегистрирован')
    def test_create_exist_user(self, user_delete_after_test, users):
        response = users.create_new_user(user_delete_after_test[0].json()["user"]["email"],
                                         UserGenerator.generate_random_string(self, 10),
                                         user_delete_after_test[0].json()["user"]["name"])

        assert (response.status_code == 403 and not response.json()["success"] and
                response.json()["message"] == ResponseMessages.USER_EXIST)


