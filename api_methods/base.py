import requests
import allure
from data import Urls

class Base:

    @staticmethod
    @allure.step('Отправляем POST запрос на end point {api}')
    def post_method(api, headers=None, body=None):
        return requests.post(Urls.MAIN_URL+api, headers=headers, data=body)

    @staticmethod
    @allure.step('Отправляем DELETE запрос на end point {api}')
    def delete_method(api, headers=None, body=None):
        return requests.delete(Urls.MAIN_URL+api, headers=headers, data=body)

    @staticmethod
    @allure.step('Отправляем GET запрос на end point {api}')
    def get_method(api, headers=None):
        return requests.get(Urls.MAIN_URL+api, headers=headers)

    @staticmethod
    @allure.step('Отправляем PATCH запрос на end point {api}')
    def patch_method(api, headers=None, body=None):
        return requests.patch(Urls.MAIN_URL+api, headers=headers, data=body)
