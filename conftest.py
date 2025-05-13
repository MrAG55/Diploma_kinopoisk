import os
import json
import pytest
from selenium import webdriver

COOKIE_PATH = os.path.join(os.path.dirname(__file__), "utils/cookies.json")


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.kinopoisk.ru")

    if os.path.exists(COOKIE_PATH) and os.path.getsize(COOKIE_PATH) > 2:
        with open(COOKIE_PATH, "r", encoding="utf-8") as f:
            cookies = json.load(f)
            for cookie in cookies:
                cookie.pop("sameSite", None)
                try:
                    driver.add_cookie(cookie)
                except Exception as e:
                    print(f"Ошибка добавления cookie: {e}")

        driver.refresh()

    yield driver
    driver.quit()
