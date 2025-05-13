

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.rate_button = (By.XPATH, "//button[contains(., 'Оценить фильм')]")
        self.rating_option = lambda rating: (
            By.XPATH,
            f"//button[contains(@aria-label, 'Оценка {rating}')]")

        self.cast_link = (By.XPATH, "//a[contains(@href, '/cast/') "
                                    "and contains(text(), 'В главных ролях')]")
        self.favorite_button = (By.XPATH, "//button[@title='Буду смотреть']")
        self.posters_link = (By.XPATH, "//a[contains(@href, '/posters/') "
                                       "and text()='постеры']")

        self.description_tab = (By.XPATH, "//span[contains(text(), 'Обзор')]")
        self.description_block = (By.XPATH, "//section[contains(@class, "
                                            "'styles_descriptionSection')]")

        self.production_year_label = (By.XPATH, "//div[contains(text(), "
                                                "'Год производства')]")

    @allure.step("Нажимаем кнопку 'Оценить фильм'")
    def click_rate_button(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
        btn = self.wait.until(EC.element_to_be_clickable(self.rate_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)

    @allure.step("Выбираем рейтинг {rating}")
    def select_rating(self, rating: int):
        locator = self.rating_option(rating)
        btn = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)

    @allure.step("Открываем раздел 'В главных ролях'")
    def click_cast(self):
        (self.driver.execute_script
         ("window.scrollTo(0, document.body.scrollHeight);"))
        self.wait.until(EC.presence_of_element_located(self.cast_link))
        link = self.driver.find_element(*self.cast_link)
        (self.driver.execute_script
         ("arguments[0].scrollIntoView({block: 'center'});", link))
        self.wait.until(EC.element_to_be_clickable(self.cast_link))
        self.driver.execute_script("arguments[0].click();", link)

    @allure.step("Нажимаем кнопку 'Буду смотреть'")
    def click_favorite(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.favorite_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)

    @allure.step("Открываем страницу постеров")
    def click_posters_link(self):
        posters = (self.wait.until
                   (EC.element_to_be_clickable(self.posters_link)))
        (self.driver.execute_script
         ("arguments[0].scrollIntoView(true);", posters))
        self.driver.execute_script("arguments[0].click();", posters)

    @allure.step("Проверяем, что описание фильма отображается")
    def has_description(self):
        overview_tab = (self.wait.until
                        (EC.element_to_be_clickable(self.description_tab)))
        (self.driver.execute_script
         ("arguments[0].scrollIntoView(true);", overview_tab))
        return self.wait.until(EC.presence_of_element_located
                               (self.description_block))

    @allure.step("Проверяем, что на странице есть блок 'Год производства'")
    def has_production_year(self):
        self.wait.until(EC.presence_of_element_located
                        (self.production_year_label))
        return True
