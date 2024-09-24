from playwright.sync_api import Playwright, sync_playwright, expect


class Zv:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
    def open_page(self):
        self. page.goto("https://zolotiyvik.ua/ru/")
        return self
    def close_help(self):
        self.page.frame_locator("iframe[name=\"helpcrunch-iframe\"]").locator(
            "[data-test-id=\"popup_close_button\"]").get_by_role("img").click()
        return self
    def change_language(self):
        self.page.get_by_role("link", name="Укр", exact=True).click()
        return self
    def open_catalog(self):
        self.page.get_by_role("banner").get_by_text("Каталог товарів").click()
        return self

    def add_ring(self):
        self.page.get_by_role("link", name="Каблучки", exact=True).nth(1).click()
        self.page.get_by_role("link", name="Біле золото Біле золото").click()
        self.page.get_by_role("link", name="Золота обручка класична. Артикул 10172б -55%").click()
        self.page.get_by_text("16.5").click()
        self.page.get_by_role("button", name="Додати в кошик").click()
        self.page.locator("#close-dropdown-minicart").get_by_role("img").click()
        return self
    def open_basket(self):
        self.page.get_by_text("Кошик 1 1items").click()
        return self
    def delete_ring(self):
        self.page.get_by_role("link", name="Видалити елемент").click()
        self.page.get_by_role("button", name="Так").click()
        self.page.locator("#close-dropdown-minicart").get_by_role("img").click()
        return self
    def close(self):
        self.page.close()
        self.browser.close()

