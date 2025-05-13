# Диплом: Автоматизация UI и API тестов для Кинопоиска

Этот проект представляет собой дипломную работу по автоматизации UI и API тестирования, основанную на финальной ручной проверке веб-приложения Кинопоиск.

## Стек технологий

- Python
- Pytest
- Selenium (UI)
- Requests (API)
- Allure (репорты)
- Page Object

## Структура проекта

config/          # настройки (базовые URL, токены и пр.)
data/            # тестовые данные
pages/           # Page Object классы
tests/           # UI и API тесты
utils/           # cookies и вспомогательные файлы
conftest.py      # фикстуры и общие настройки
requirements.txt # зависимости
README.md        # описание проекта

## Как запустить тесты

1. Установить зависимости:
pip install -r requirements.txt

2. Запустить UI-тесты:
pytest tests/test_ui.py

3. Запустить API-тесты:
pytest tests/test_api.py

4. Сформировать Allure-отчёт:
pytest --alluredir=allure-results
allure serve allure-results

## Связанный проект

-  Финальный проект по ручному тестированию Кинопоиска:  
  [https://mrag.yonote.ru/doc/finalnyj-proekt-po-ruchnomu-testirovaniyu-kinopoisk-DD4m7RFw3a](https://mrag.yonote.ru/doc/finalnyj-proekt-po-ruchnomu-testirovaniyu-kinopoisk-DD4m7RFw3a)

- Автоматизация тестирования на основе этой работы:
  [GitHub: MrAG55/Diploma_kinopoisk](https://github.com/MrAG55/Diploma_kinopoisk)
