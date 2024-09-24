from playwright.sync_api import sync_playwright
from models.zv import Zv


def test_z():
    with sync_playwright() as playwright:
        best_zv = Zv(playwright)
        best_zv.open_page()
        # best_zv.close_help()
        best_zv.change_language()
        best_zv.open_catalog()
        best_zv.add_ring()
        best_zv.open_basket()
        best_zv.delete_ring()
        best_zv.close()
