from selenium.webdriver.common.by import By
from constants import Test_URL
import allure


@allure.title("Поиск фильма на кириллице ")
@allure.description("Тест поиск фильма на кириллице")
@allure.severity("Критический")
def test_search_film(driver):
    driver.get(Test_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Криминальное чтиво")
    driver.find_element(By.ID, "suggest-item-film-342").click()
    assert driver.find_element(
        By.CSS_SELECTOR,
        "span[data-tid='75209b22']").text == "Криминальное чтиво (1994)"


@allure.title("Поиск фильма на латинице")
@allure.description("Тест поиск фильма на латинице")
@allure.severity("Критический")
def test_search_english_film(driver):
    driver.get(Test_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Pulp Fiction")
    driver.find_element(By.ID, "suggest-item-film-342").click()
    assert driver.find_element(
        By.CSS_SELECTOR, 
        "span[data-tid='75209b22']").text == "Криминальное чтиво (1994)"


@allure.title("Поиск фильма на транслите")
@allure.description("Тест поиск фильма на транслите")
@allure.severity("Критический")
def test_search_translit_film(driver):
    driver.get(Test_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Kriminalnoe chtivo")
    driver.find_element(By.ID, "suggest-item-film-342").click()
    assert driver.find_element(
        By.CSS_SELECTOR, 
        "span[data-tid='75209b22']").text == "Криминальное чтиво (1994)"


@allure.title("Поиск персоны на кириллице")
@allure.description("Тест поиск персоны на кириллице")
@allure.severity("Критический")
def test_search_person(driver):
    driver.get(Test_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Ума Турман")
    driver.find_element(By.ID, "suggest-item-person-29595").click()
    assert driver.find_element(
        By.CSS_SELECTOR, "h1[data-tid='f22e0093']").text == "Ума Турман"


@allure.title("Поиск персоны на латинице")
@allure.description("Тест поиск персоны на латинице")
@allure.severity("Критический")
def test_search_person_english(driver):
    driver.get(Test_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Uma Thurman")
    driver.find_element(By.ID, "suggest-item-person-29595").click()
    assert driver.find_element(
        By.CSS_SELECTOR, "h1[data-tid='f22e0093']").text == "Ума Турман"
