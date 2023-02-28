import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Test_Entry:
    @pytest.mark.parametrize("driver", ['https://stellarburgers.nomoreparties.site/'], indirect=True)
    def test_entry_by_login_button(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))).click()
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
        self, driver.find_element(By.XPATH, "//input[@name='name']").send_keys('kathryn64@example.net')
        self, driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('eN3G2w')
        self, driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        assert (WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))).text == 'Оформить заказ'


    @pytest.mark.parametrize("driver", ['https://stellarburgers.nomoreparties.site/'], indirect=True)
    def test_entry_by_personal_area_button(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))).click()
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
        self, driver.find_element(By.XPATH, "//input[@name='name']").send_keys('kathryn64@example.net')
        self, driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('eN3G2w')
        self, driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        assert (WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))).text == 'Оформить заказ'


    @pytest.mark.parametrize("driver", ['https://stellarburgers.nomoreparties.site/register'], indirect=True)
    def test_entry_by_button_registration_form(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))).click()
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
        self, driver.find_element(By.XPATH, "//input[@name='name']").send_keys('kathryn64@example.net')
        self, driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('eN3G2w')
        self, driver.find_element(By.XPATH, "//button[text()='Войти']").click()  # Кнопка «Войти»
        assert (WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))).text == 'Оформить заказ'


    @pytest.mark.parametrize("driver", ['https://stellarburgers.nomoreparties.site/forgot-password'], indirect=True)
    def test_entry_by_button_password_recovery_form(self, driver):
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))).click()
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
        self, driver.find_element(By.XPATH, "//input[@name='name']").send_keys('kathryn64@example.net')
        self, driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('eN3G2w')
        self, driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        assert (WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))).text == 'Оформить заказ'
