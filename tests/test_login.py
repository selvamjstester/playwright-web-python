import pytest

from config import Config
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.login
def test_valid_login_lands_on_inventory(login_page):
    login_page.login(Config.STANDARD_USER, Config.PASSWORD)
    inventory = InventoryPage(login_page.page)
    assert inventory.title() == "Products"
    assert inventory.item_count() == 6


@pytest.mark.login
def test_locked_out_user_sees_error(login_page):
    login_page.login(Config.LOCKED_USER, Config.PASSWORD)
    assert login_page.has_error()
    assert "locked out" in login_page.error_message().lower()


@pytest.mark.login
def test_invalid_password_shows_error(login_page):
    login_page.login(Config.STANDARD_USER, "wrong_password")
    assert login_page.has_error()
    assert "do not match" in login_page.error_message().lower()
