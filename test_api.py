import requests
import allure
from constants import *


@allure.title("Поиск фильма по названию на кириллице")
@allure.description("Тест проверяет поиск сериала по названию на кириллице")
@allure.severity("Критический")
def test_search_film():
    with allure.step("Создание хедеров"):
        json = {
            "X-API-KEY": Token
        }
    with allure.step("Отправка запроса"):
        response = requests.get(
            f"{{BaseURL}}/movie/"
            "search?page=1&limit=10&query=Великолепный Век",
            headers=json)
    with allure.step("Проверка результата"):
        assert response.status_code == 200


@allure.title("Поиск фильма по названию на латинице")
@allure.description("Тест проверяет поиск сериала по названию на латинице")
@allure.severity("Критический")
def test_search_film_englisn():
    with allure.step("Создание хедеров"):
        json = {
            "X-API-KEY": Token
        }
    with allure.step("Отправка запроса"):
        response = requests.get(
            f"{{BaseURL}}/movie/"
            "search?page=1&limit=10&query=Muhtesem Yüzyil",
            headers=json)
    with allure.step("Проверка результата"):
        assert response.status_code == 200


@allure.title("Поиск фильма по id")
@allure.description("Тест проверяет поиск фильма по id")
@allure.severity("Критический")
def test_search_id():
    with allure.step("Создание хедеров"):
        json = {
            "X-API-KEY": Token
        }
    response = requests.get(
        f"{{BaseURL}}/movie/924910", headers=json)

    assert response.status_code == 200

    assert response.json()[
               "description"] == ("История королевы Елизаветы II "
                                  "с момента её свадьбы в 1947 году"
                                  " до настоящего времени.")


@allure.title("Поиск фильма по id актера")
@allure.description("Тест проверяет поиск фильма по id актера")
@allure.severity("Критический")
def test_search_id_person():
    json = {
        "X-API-KEY": Token
    }
    response = requests.get(
        f"{{BaseURL}}/person/896879", headers=json)

    assert response.status_code == 200


@allure.title("Поиск картинки")
@allure.description("Тест проверяет поиск картинки")
@allure.severity("Критический")
def test_search_id_picture():
    json = {
        "X-API-KEY": Token
    }
    response = requests.get(
        f"{{BaseURL}}/image?page=1&limit=1", headers=json)

    assert response.status_code == 200
