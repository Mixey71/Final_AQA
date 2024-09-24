import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://zolotiyvik.ua/ru/")
        # page.frame_locator("iframe[name=\"helpcrunch-iframe\"]").locator(
        #     "[data-test-id=\"popup_close_button\"]").get_by_role("img").click()
        page.get_by_role("link", name="Укр", exact=True).click()
        page.get_by_role("banner").get_by_text("Каталог товарів").click()
        page.get_by_role("link", name="Каблучки", exact=True).nth(1).click()
        page.get_by_role("link", name="Біле золото Біле золото").click()
        page.get_by_role("link", name="Золота каблучка з фіанітами. Артикул UG5110128110201 -29%").click()
        page.get_by_text("16.5").click()
        page.get_by_role("button", name="Додати в кошик").click()
        page.locator("#close-dropdown-minicart").get_by_role("img").click()
        page.get_by_text("Кошик 1 1items").click()
        page.get_by_role("link", name="Видалити елемент").click()
        page.get_by_role("button", name="Так").click()
        page.locator("#close-dropdown-minicart").get_by_role("img").click()

        browser.close()
