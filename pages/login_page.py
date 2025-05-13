

import os
import json
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COOKIE_PATH = os.path.join(os.path.dirname(__file__), "../utils/cookies.json")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.url = "https://www.kinopoisk.ru/"

    @allure.step("Открываем главную страницу")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Нажимаем 'Войти'")
    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Войти')]")
        ))
        login_button.click()

    @allure.step("Нажимаем 'Ещё' и 'Войти по логину'")
    def select_login_by_email(self):
        more_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Ещё']")
        ))
        self.driver.execute_script("arguments[0].click();", more_button)

        login_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Войти по')]")
        ))
        login_option.click()

    @allure.step("Вводим логин и нажимаем 'Войти'")
    def enter_email(self, email):
        email_input = self.wait.until(EC.presence_of_element_located(
            (By.ID, "passp-field-login")
        ))
        email_input.send_keys(email)

        login_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Войти']")
        ))
        self.driver.execute_script("arguments[0].click();", login_button)

    @allure.step("Вводим пароль и нажимаем 'Продолжить'")
    def enter_password(self, password):
        password_input = self.wait.until(EC.presence_of_element_located(
            (By.ID, "passp-field-passwd")
        ))
        password_input.send_keys(password)

        continue_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Продолжить']")
        ))
        self.driver.execute_script("arguments[0].click();", continue_button)

    @allure.step("Сохраняем куки в файл после входа")
    def save_cookies(self):
        cookies = self.driver.get_cookies()
        with open(COOKIE_PATH, "w", encoding="utf-8") as f:
            json.dump(cookies, f, indent=2)

    @allure.step("Проходим авторизацию и возвращаемся на Кинопоиск")
    def login(self, email, password):
        self.click_login_button()
        self.select_login_by_email()
        self.enter_email(email)
        self.enter_password(password)

        self.wait.until(EC.title_contains("Авторизация"))
        self.driver.get("https://www.kinopoisk.ru/")

        self.save_cookies()
