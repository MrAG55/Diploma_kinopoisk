from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.cast_link = (By.XPATH, "//a[contains(@href,'/cast/')]")

        self.favorite_button = (By.XPATH, "//button[@title='Буду смотреть']")

        self.production_year_label = (
            By.XPATH,
            "//div[contains(text(),'Год производства')]"
        )

    @allure.step("Открываем раздел 'В главных ролях'")
    def click_cast(self):

        link = (self.wait.until
                (EC.visibility_of_element_located(self.cast_link)))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", link
        )

        self.driver.execute_script("arguments[0].click();", link)

    @allure.step("Нажимаем кнопку 'Буду смотреть' (если присутствует)")
    def click_favorite(self):
        try:
            btn = (self.wait.until
                   (EC.visibility_of_element_located(self.favorite_button)))
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", btn
            )
            self.driver.execute_script("arguments[0].click();", btn)
        except TimeoutException:

            pass

    @allure.step("Проверяем, что на странице есть блок 'Год производства'")
    def has_production_year(self):
        self.wait.until(EC.presence_of_element_located
                        (self.production_year_label))
        return True
