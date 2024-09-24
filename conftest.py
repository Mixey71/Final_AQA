from playwright.sync_api import Playwright, sync_playwright, expect
from pytest import fixture
from models.zv import Zv


@fixture()
def get_tes():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def best_zv(get_tes):
    zv = Zv(get_tes)
    yield zv
    zv.close()