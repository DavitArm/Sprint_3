import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize("driver", ['https://stellarburgers.nomoreparties.site/'], indirect=True)
class Test_transitions_to_sections:
    def test_transition_the_section_Sauces(self, driver):
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h1[text() = 'Соберите бургер']")))
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//span[text() = 'Соусы']"))).click()
        assert WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Соусы']"))).text == 'Соусы'


    def test_transition_the_section_toppings(self, driver):
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h1[text() = 'Соберите бургер']")))
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//span[text() = 'Начинки']"))).click()
        assert WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Начинки']"))).text == 'Начинки'


    def test_transition_the_section_rolls(self, driver):
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h1[text() = 'Соберите бургер']")))
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//span[text() = 'Соусы']"))).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//span[text() = 'Булки']"))).click()
        assert WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Булки']"))).text == 'Булки'
