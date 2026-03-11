from playwright.sync_api import expect
import time

class CartPage:

    def __init__(self, page):

        self.page = page
        self.cart = page.locator("#sc-active-cart")

    def open_cart(self):

        print("Opening Amazon cart page...")
        self.page.goto("https://www.amazon.de/cart")
        print("✓ Cart page opened.\n")

    def verify_cart_visible(self):

        print("Verifying that the cart is visible...")

        expect(self.cart).to_be_visible()

        print("✓ Cart is visible.\n")

    def delete_item(self):

        print("Removing all items from cart...")

        delete_buttons = self.page.locator("input[data-action='delete-active']")

        while delete_buttons.count() > 0:
            delete_buttons.first.click()
            self.page.wait_for_timeout(2000)

        print("✓ Cart emptied.\n")