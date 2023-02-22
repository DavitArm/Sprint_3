import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize("driver", ['https://stellarburgers.nomoreparties.site/login'], indirect=True)
class Test_transition:
    def test_transition_by_clicking_on_personal_account(self, driver):
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
        self, driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('kathryn64@example.net')
        self, driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('eN3G2w')
        self, driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//p[text() = 'Личный Кабинет']"))).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, ".//a[text() = 'Профиль']")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'


    def test_transition_by_click_from_personal_account_to_the_constructor(self, driver):
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
        self, driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('kathryn64@example.net')
        self, driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('eN3G2w')
        self, driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//p[text() = 'Личный Кабинет']"))).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//p[text() = 'Конструктор']"))).click()
        assert (WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))).text == 'Оформить заказ'


    def test_transition_by_click_from_personal_account_to_the_stellar_burgers_logo(self, driver):
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
        self, driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('kathryn64@example.net')
        self, driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('eN3G2w')
        self, driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//p[text() = 'Личный Кабинет']"))).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//div[@class ='AppHeader_header__logo__2D0X2']"))).click()
        assert (WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))).text == 'Оформить заказ'
