import allure

from data import ResponseMessages


class TestUpdateUserData:

    @allure.title('Тест обновления имени пользователя с авторизацией')
    @allure.description('Тест проверяет ответы API на попытку изменить имя пользователя с авторизацией')
    def test_update_user_data_name_with_auth(self, user_delete_after_test, users, new_user_data):
        users.update_user_data(user_delete_after_test[0].json()["accessToken"], name=new_user_data["name"])
        response = users.get_user_data(user_delete_after_test[0].json()["accessToken"])

        assert response.status_code == 200 and response.json()["user"]["name"] == new_user_data["name"]

    @allure.title('Тест обновления email пользователя с авторизацией')
    @allure.description('Тест проверяет ответы API на попытку изменить email пользователя с авторизацией')
    def test_update_user_data_email_with_auth(self, user_delete_after_test, users, new_user_data):
        users.update_user_data(user_delete_after_test[0].json()["accessToken"], email=new_user_data["email"])
        response = users.get_user_data(user_delete_after_test[0].json()["accessToken"])

        assert response.status_code == 200 and response.json()["user"]["email"] == new_user_data["email"]

    @allure.title('Тест обновления пароля пользователя с авторизацией')
    @allure.description('Тест проверяет ответы API на попытку изменить пароль пользователя с авторизацией')
    def test_update_user_data_password_with_auth(self, user_delete_after_test, users, new_user_data):
        users.update_user_data(user_delete_after_test[0].json()["accessToken"], password=new_user_data["password"])
        users.logout_user(user_delete_after_test[0].json()["refreshToken"])

        response = users.login_user(user_delete_after_test[1]["email"], new_user_data["password"])

        assert response.status_code == 200 and response.json()["success"]

    @allure.title('Тест обновления имени пользователя без авторизации')
    @allure.description('Тест проверяет ответы API на попытку изменить имя пользователя без авторизации')
    def test_update_user_data_name_without_auth(self, user_delete_after_test, users, new_user_data):
        response = users.update_user_data(name=new_user_data["name"])

        assert (response.status_code == 401 and not response.json()["success"] and
                response.json()["message"] == ResponseMessages.UPDATE_USER_DATA_WITHOUT_AUTH)

    @allure.title('Тест обновления email пользователя без авторизации')
    @allure.description('Тест проверяет ответы API на попытку изменить email пользователя без авторизации')
    def test_update_email_data_name_without_auth(self, user_delete_after_test, users, new_user_data):
        response = users.update_user_data(email=new_user_data["email"])

        assert (response.status_code == 401 and not response.json()["success"] and
                response.json()["message"] == ResponseMessages.UPDATE_USER_DATA_WITHOUT_AUTH)

    @allure.title('Тест обновления пароля пользователя без авторизации')
    @allure.description('Тест проверяет ответы API на попытку изменить пароля пользователя без авторизации')
    def test_update_user_data_password_without_auth(self, user_delete_after_test, users, new_user_data):
        response = users.update_user_data(password=new_user_data["password"])

        assert (response.status_code == 401 and not response.json()["success"] and
                response.json()["message"] == ResponseMessages.UPDATE_USER_DATA_WITHOUT_AUTH)

