from selenium import webdriver
from pages.login_page import LoginPage
from data.test_data import TEST_USER_EMAIL, TEST_USER_PASSWORD


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    login = LoginPage(driver)
    login.open()
    login.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    input("После прохождения капчи и входа нажми Enter для сохранения cookies")
    login.save_cookies()
    print("Cookies успешно сохранены.")
    driver.quit()


if __name__ == "__main__":
    main()
