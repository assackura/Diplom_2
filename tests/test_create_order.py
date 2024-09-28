import allure
from data import ResponseMessages

class TestCreateOrder:

    @allure.title('Тест создания нового заказа авторизованным пользователем')
    @allure.description('Тест проверяет ответы API на попытку создать новый заказ авторизованным пользователем')
    def test_create_order_with_login(self, receipt, user_delete_after_test, orders):
        response = orders.create_new_order(receipt, user_delete_after_test[0].json()["accessToken"])

        assert response.status_code == 200 and response.json()["success"]

    @allure.title('Тест создания нового заказа неавторизованным пользователем')
    @allure.description('Тест проверяет ответы API на попытку создать новый заказ неавторизованным пользователем')
    def test_create_order_without_login(self, receipt, orders):
        response = orders.create_new_order(receipt)

        assert response.status_code == 200 and response.json()["success"]

    @allure.title('Тест создания нового заказа с ингридиентами')
    @allure.description('Тест проверяет ответы API на попытку создать новый заказ с ингридиентами')
    def test_create_order_with_ing(self, receipt, orders):
        response = orders.create_new_order(receipt)

        assert response.status_code == 200 and response.json()["success"]

    @allure.title('Тест создания нового заказа без ингридиентов')
    @allure.description('Тест проверяет ответы API на попытку создать новый заказ без указания ингридиентов')
    def test_create_order_without_ing(self, orders):
        response = orders.create_new_order()

        assert (response.status_code == 400 and not response.json()["success"] and
                response.json()["message"] == ResponseMessages.CREATE_ORDER_WITHOUT_ING)

    @allure.title('Тест создания нового заказа с некорректными ингридиентами')
    @allure.description('Тест проверяет ответы API на попытку создать новый заказ с некорректными hash ингридиентов')
    def test_create_order_with_incorrect_hash_ing(self, orders):
        response = orders.create_new_order(["sdfsdfsd", "sdfsdfsdfwef"])

        assert response.status_code == 500

