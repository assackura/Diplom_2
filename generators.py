import string
import random


class UserGenerator:

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email(self):
        letters = string.ascii_lowercase
        random_email = ''.join(random.choice(letters) for i in range(5))
        random_email += '@'
        random_email += ''.join(random.choice(letters) for i in range(5))
        random_email += '.'
        random_email += ''.join(random.choice(letters) for i in range(2))
        return random_email

class GenerateReceipt:

    def generate_receipt(self, array):
        random_receipt = []
        for i in range(4):
            random_receipt.append(array[random.randint(0, len(array) - 1)]["_id"])
        return random_receipt