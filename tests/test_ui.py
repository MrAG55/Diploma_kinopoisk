

from pages.login_page import LoginPage
from data.test_data import TEST_USER_EMAIL, TEST_USER_PASSWORD


def test_login_valid_user(driver):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    assert "Кинопоиск" in driver.title
