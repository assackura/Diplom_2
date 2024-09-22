import random
from http.client import responses

import pytest

from api_methods.orders import Orders
from generators import UserGenerator, GenerateReceipt
from api_methods.users import User


@pytest.fixture(scope='function')
def new_user_data():
    generator = UserGenerator()
    login_pass = {"email": generator.generate_random_email(),
                  "password": generator.generate_random_string(10),
                  "name": generator.generate_random_string(10)}
    return login_pass

@pytest.fixture(scope='function')
def users():
    user = User()
    return user

@pytest.fixture(scope='function')
def orders():
    order = Orders()
    return order

@pytest.fixture(scope='function')
def receipt(orders):
    generator = GenerateReceipt()
    response = orders.get_data_of_ing()
    receipt = generator.generate_receipt(response.json()["data"])
    return receipt

@pytest.fixture(scope='function')
def user_delete_after_test(new_user_data, users):
    response = users.create_new_user(new_user_data["email"], new_user_data["password"], new_user_data["name"])

    yield response, new_user_data

    users.delete_user(response.json()["accessToken"])

@pytest.fixture(scope='function')
def order_for_user(user_delete_after_test, orders, receipt):
    response = orders.create_new_order(receipt, user_delete_after_test[0].json()["accessToken"])
    return user_delete_after_test