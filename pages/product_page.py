from playwright.sync_api import expect
import time

class ProductPage:

    def __init__(self, page):

        self.page = page
        self.title = page.locator("span#productTitle")
        self.add_to_cart = page.get_by_role("button", name="Add to basket", exact=True)
        self.product_protection = page.get_by_role("button", name="No, thank you")

    def verify_product_page(self):

        print("Verifying product page has loaded...")

        expect(self.title).to_be_visible()

        product_name = self.title.inner_text()
        print(f"✓ Product page loaded: {product_name}\n")

    def add_product_to_cart(self):

        print("Attempting to add product to cart...")
        self.page.mouse.wheel(0, 400)

        self.add_to_cart.click()
        print("✓ 'Add to basket' button clicked.")
        time.sleep(5)
        try:
            print("Checking for product protection popup...")
            self.product_protection.click()
            print("✓ Product protection declined.")
        except:
            print("No product protection popup appeared.")

        print("Product successfully added to cart.\n")
    
    def get_product_price(self):

        price = self.page.locator("span.a-price-whole").first.inner_text()

        return price