from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.search_input = (By.NAME, "kp_query")

    @allure.step("Вводим название фильма в поиск")
    def search_film(self, title: str):
        inp = self.wait.until(EC.presence_of_element_located
                              (self.search_input))
        inp.clear()
        inp.send_keys(title)
        inp.send_keys(Keys.ENTER)

    @allure.step("Кликаем на фильм по заголовку '{title}'")
    def click_film_by_title(self, title: str):
        locator = \
            (By.XPATH, f"//a[contains(@href, '/film/')"
                       f" and contains(text(), '{title}')]")
        film = self.wait.until(EC.element_to_be_clickable(locator))
        film.click()
