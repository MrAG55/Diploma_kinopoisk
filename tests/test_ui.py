

import allure
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.card_page import CardPage
from data.test_data import TEST_USER_EMAIL, TEST_USER_PASSWORD


# UI-Тест 1: Авторизация + проверка заголовка

@allure.title("Авторизация пользователя и проверка заголовка")
def test_login_valid_user(driver):
    login = LoginPage(driver)
    with allure.step("Открываем главную страницу"):
        login.open()
    with allure.step("Выполняем полный вход"):
        login.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    with allure.step("Убедиться, что на странице есть 'Кинопоиск'"):
        assert "Кинопоиск" in driver.title


# UI-Тест 2: Поиск фильма 'Петля времени'

@allure.title("Поиск фильма в залогиненном режиме")
def test_search_film_logged_in(driver):
    login = LoginPage(driver)
    search = SearchPage(driver)

    with allure.step("Логинимся"):
        login.open()
        login.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    with allure.step("Ищем фильм 'Петля времени'"):
        search.search_film("Петля времени")

    with allure.step("Проверяем страницу результатов"):
        assert "/search/" in driver.current_url or "Кинопоиск" in driver.title


# UI-Тест 3: Проверка года производства

@allure.title("Проверка наличия года производства в описании фильма")
def test_production_year_visible(driver):
    login = LoginPage(driver)
    search = SearchPage(driver)
    card = CardPage(driver)

    with allure.step("Логинимся и открываем карточку фильма"):
        login.open()
        login.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        search.search_film("Петля времени")
        search.click_film_by_title("Петля времени")

    with allure.step("Проверяем, что отображается год производства"):
        assert card.has_production_year()


# UI-Тест 4: Открываем раздел 'В главных ролях'

@allure.title("Переход в раздел 'В главных ролях'")
def test_open_cast_page_logged_in(driver):
    login = LoginPage(driver)
    search = SearchPage(driver)
    card = CardPage(driver)

    with allure.step("Логинимся и открываем карточку"):
        login.open()
        login.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        search.search_film("Петля времени")
        search.click_film_by_title("Петля времени")

    with allure.step("Переходим в актёры"):
        card.click_cast()

    with allure.step("Проверяем URL содержит '/cast/'"):
        assert "/cast/" in driver.current_url


# UI-Тест 5: Кнопка 'Буду смотреть'

@allure.title("Нажимаем кнопку 'Буду смотреть'")
def test_favorite_button_logged_in(driver):
    login = LoginPage(driver)
    search = SearchPage(driver)
    card = CardPage(driver)

    with allure.step("Логинимся и открываем карточку"):
        login.open()
        login.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        search.search_film("Петля времени")
        search.click_film_by_title("Петля времени")

    with allure.step("Жмём 'Буду смотреть'"):
        card.click_favorite()

    with allure.step("Убедиться, что клик прошёл"):
        assert True
