from faker import Faker


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_correct = {
        "email": 'polov1111@yandex.ru',
        "password": "123456"}

    data_negative = {
        "email": 'polovm@yandex.ru',
        "password": "123456"}

    data_double = {
        "email": 'polov1111@yandex.ru',
        "password": "password",
        "name": "Username"}

    data_without_email = {
        "email": '',
        "password": "password",
        "name": "Username"}

    data_without_password = {
        "email": 'polov1111@yandex.ru',
        "password": "",
        "name": "Username"}

    data_without_name = {
        "email": 'polov1111@yandex.ru',
        "password": "12345678",
        "name": ""}

    data_updated = {
        "email": 'polov11111@yandex.ru',
        "password": "password",
        "name": "Test"}