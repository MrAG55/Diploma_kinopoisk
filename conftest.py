

import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def base_url():
    from config.settings import BASE_URL
    return BASE_URL

@pytest.fixture(scope="function")
def driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def api_headers():

    return {
        "Content-Type": "application/json"
    }
