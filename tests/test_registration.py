import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Test_registration:
    @pytest.mark.parametrize("driver", ['https://stellarburgers.nomoreparties.site/register'], indirect=True)
    def test_registration(self, driver, email, password):
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))).send_keys(
            'User name')
        self, driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
        self, driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        self, driver.find_element(By.XPATH,"//button[text() = 'Зарегистрироваться']").click()
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
        self, driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
        self, driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        self, driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//p[text() = 'Личный Кабинет']"))).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, "//a[text() = 'Профиль']")))
        assert len(password) >= 6, "Минимальный пароль 6 символов"
        assert driver.find_element(By.XPATH, "//input[@name = 'Name']").get_attribute('value') == 'User name' and \
               driver.find_element(By.XPATH, "//label[text()='Логин']/following-sibling::input").get_attribute('value') == email
