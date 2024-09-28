import allure

from data import ResponseMessages

class TestGetOrders:

    @allure.title('Тест получения списка заказов пользователя с авторизацией')
    @allure.description('Тест проверяет ответы API на попытку получить список заказов пользователя с авторизацией')
    def test_get_orders_user_with_auth(self, order_for_user, orders):
        response = orders.get_orders(order_for_user[0].json()["accessToken"])

        assert response.json()["success"]

    @allure.title('Тест получения списка заказов пользователя без авторизации')
    @allure.description('Тест проверяет ответы API на попытку получить список заказов пользователя без авторизации')
    def test_get_orders_user_without_auth(self, orders):
        response = orders.get_orders()

        assert (response.status_code == 401 and not response.json()["success"] and
                response.json()["message"] == ResponseMessages.UPDATE_USER_DATA_WITHOUT_AUTH)