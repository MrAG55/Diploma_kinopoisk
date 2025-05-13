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

    @allure.step("Проверяем, что пользователь уже залогинен по наличию cookie")
    def is_logged_in(self) -> bool:
        return any(c.get("name") == "desktop_session_key"
                   for c in self.driver.get_cookies())

    @allure.step("Применяем сохранённые куки для авторизации")
    def apply_cookies(self):
        if not os.path.exists(COOKIE_PATH):
            raise RuntimeError(f"Файл с куки не найден: {COOKIE_PATH}")
        self.driver.get(self.url)
        with open(COOKIE_PATH, "r", encoding="utf-8") as f:
            cookies = json.load(f)
        for cookie in cookies:
            cookie.pop("sameSite", None)
            cookie.pop("domain", None)
            try:
                self.driver.add_cookie(cookie)
            except Exception:
                pass
        self.driver.refresh()

    @allure.step("Нажимаем 'Войти'")
    def click_login_button(self):
        btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Войти')]")
        ))
        btn.click()

    @allure.step("Нажимаем 'Ещё' → 'Войти по логину'")
    def select_login_by_email(self):
        more = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Ещё']")))
        self.driver.execute_script("arguments[0].click();", more)
        by_email = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Войти по')]")))
        by_email.click()

    @allure.step("Вводим логин и нажимаем 'Войти'")
    def enter_email(self, email):
        inp = self.wait.until(EC.presence_of_element_located(
            (By.ID, "passp-field-login")))
        inp.send_keys(email)
        ok = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Войти']")))
        self.driver.execute_script("arguments[0].click();", ok)

    @allure.step("Вводим пароль и нажимаем 'Продолжить'")
    def enter_password(self, password):
        inp = self.wait.until(EC.presence_of_element_located(
            (By.ID, "passp-field-passwd")))
        inp.send_keys(password)
        cont = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Продолжить']")))
        self.driver.execute_script("arguments[0].click();", cont)

    @allure.step("Сохраняем куки в файл")
    def save_cookies(self):
        cookies = self.driver.get_cookies()
        with open(COOKIE_PATH, "w", encoding="utf-8") as f:
            json.dump(cookies, f, indent=2)

    @allure.step("Ручная авторизация и сохранение куки")
    def login_and_save_cookies(self, email, password):
        self.open()
        self.click_login_button()
        self.select_login_by_email()
        self.enter_email(email)
        self.enter_password(password)
        self.wait.until(EC.title_contains("Кинопоиск"))
        self.save_cookies()
