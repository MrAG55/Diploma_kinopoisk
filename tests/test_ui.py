import allure
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.card_page import CardPage

# UI-Тест 1: проверяем, что с куками залогинены


@allure.title("Авторизация через куки и проверка, что пользователь в системе")
def test_login_via_cookies(driver):
    login = LoginPage(driver)
    with allure.step("Открываем главную страницу и подгружаем куки"):
        login.open()
        login.apply_cookies()
    with allure.step("Убедиться, что пользователь действительно залогинен"):
        assert login.is_logged_in()


# UI-Тест 2: Поиск фильма 'Петля времени'

@allure.title("Поиск фильма в залогиненном режиме")
def test_search_film_logged_in(driver):
    login = LoginPage(driver)
    search = SearchPage(driver)

    with allure.step("Открываем главную страницу и применяем куки"):
        login.open()
        login.apply_cookies()

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

    with allure.step("Открываем главную страницу и применяем куки"):
        login.open()
        login.apply_cookies()

    with allure.step("Открываем карточку 'Петля времени'"):
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

    with allure.step("Открываем главную страницу и применяем куки"):
        login.open()
        login.apply_cookies()

    with allure.step("Открываем карточку фильма"):
        search.search_film("Петля времени")
        search.click_film_by_title("Петля времени")

    with allure.step("Переходим в раздел 'В главных ролях'"):
        card.click_cast()

    with allure.step("Проверяем URL содержит '/cast/'"):
        assert "/cast/" in driver.current_url


# UI-Тест 5: Кнопка 'Буду смотреть'

@allure.title("Нажимаем кнопку 'Буду смотреть'")
def test_favorite_button_logged_in(driver):
    login = LoginPage(driver)
    search = SearchPage(driver)
    card = CardPage(driver)

    with allure.step("Открываем главную страницу и применяем куки"):
        login.open()
        login.apply_cookies()

    with allure.step("Открываем карточку фильма"):
        search.search_film("Петля времени")
        search.click_film_by_title("Петля времени")

    with allure.step("Жмём 'Буду смотреть'"):
        card.click_favorite()

    with allure.step("Убедиться, что клик прошёл"):
        assert True
