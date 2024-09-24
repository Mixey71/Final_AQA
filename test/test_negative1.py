from playwright.sync_api import Playwright, sync_playwright, expect

def test_negative2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://zolotiyvik.ua/ru/')
        # page.frame_locator("iframe[name=\"helpcrunch-iframe\"]").locator(
        #     "[data-test-id=\"popup_close_button\"]").get_by_role("img").click()
        # page.pause()
        page.locator(".dropdown-toggle-icon-block").click()
        page.wait_for_timeout(5000)
        page.get_by_role("button", name="Отправить").click()
        expect(page.get_by_text("Это поле обязательно к заполнению.")).to_be_visible()

        browser.close()