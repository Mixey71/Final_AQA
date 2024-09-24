from playwright.sync_api import Playwright, sync_playwright, expect

def test_negative():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.ukrposhta.ua/ua")
        page.get_by_role("link", name="Реєстрація profile-icon").click()
        page.get_by_role("link", name="Вхід").click()
        page.get_by_role("button", name="Зайти").click()
        page.get_by_placeholder("E-mail").fill("hdhgf")
        page.get_by_role("button", name="Зайти").click()
        page.get_by_text("E-mail:* Пароль:* Зайти Реєстрація Забули пароль? Google Facebook").click()
        page.get_by_placeholder("Пароль").fill("hjgdhf")
        page.get_by_role("button", name="Зайти").click()
        expect(page.get_by_text("Невірне ім'я користувача")).to_be_visible()
    # ---------------------
        browser.close()

def test_negative1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://zolotiyvik.ua/ru/')
        # page.frame_locator("iframe[name=\"helpcrunch-iframe\"]").locator(
        #     "[data-test-id=\"popup_close_button\"]").get_by_role("img").click()
        # page.pause()
        page.locator(".dropdown-toggle-icon-block").click()
        page.get_by_placeholder("+380 __ ___ ____").fill('000000000000')
        page.wait_for_timeout(5000)
        page.get_by_role("button", name="Отправить").click()
        expect(page.get_by_text("Введите верный телефон.")).to_be_visible()

        browser.close()


