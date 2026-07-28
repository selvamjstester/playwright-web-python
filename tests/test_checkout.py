import pytest

from config import Config
from pages.inventory_page import InventoryPage


@pytest.fixture
def inventory(login_page):
    login_page.login(Config.STANDARD_USER, Config.PASSWORD)
    return InventoryPage(login_page.page)


@pytest.mark.smoke
@pytest.mark.checkout
def test_add_item_updates_cart_badge(inventory):
    assert inventory.cart_count() == 0
    inventory.add_backpack_to_cart()
    assert inventory.cart_count() == 1


@pytest.mark.checkout
def test_cart_opens_from_inventory(inventory):
    inventory.add_backpack_to_cart()
    inventory.open_cart()
    assert "/cart.html" in inventory.page.url
