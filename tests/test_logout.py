import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.parametrize("driver", ['https://stellarburgers.nomoreparties.site/login'], indirect=True)
class Test_logout:
    def test_logout_by_clicking_Logout_button_in_personal_account(self, driver):
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
        self, driver.find_element(By.XPATH, ".//input[@name='name']").send_keys('kathryn64@example.net')
        self, driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys('eN3G2w')
        self, driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//p[text() = 'Личный Кабинет']"))).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//button[text() = 'Выход']"))).click()
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//h2[text() = 'Вход']")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
