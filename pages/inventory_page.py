from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = ".title"
    INVENTORY_ITEM = ".inventory_item"
    ADD_TO_CART_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def title(self) -> str:
        return self.text(self.TITLE)

    def item_count(self) -> int:
        return self.page.locator(self.INVENTORY_ITEM).count()

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def cart_count(self) -> int:
        if not self.is_visible(self.CART_BADGE):
            return 0
        return int(self.text(self.CART_BADGE))

    def open_cart(self):
        self.click(self.CART_LINK)
