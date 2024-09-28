import allure

from api_methods.base import Base
from data import EndPoints

class Orders(Base):

    @allure.step('Получаем список ингредиентов')
    def get_data_of_ing(self):
        response = self.get_method(EndPoints.GET_DATA_ING)
        return response

    @allure.step('Создаем новый заказ')
    def create_new_order(self, ings=None, token=None):
        body = {
            "ingredients": ings
        }
        headers = {
            "Authorization": f"{token}"
        }
        response = self.post_method(EndPoints.GET_AND_CREATE_NEW_ORDER, headers=headers, body=body)
        return response

    @allure.step('Получаем список заказов')
    def get_orders(self, token=None):
        headers = {
            "Authorization": f"{token}"
        }
        response = self.get_method(EndPoints.GET_AND_CREATE_NEW_ORDER, headers=headers)
        return response
