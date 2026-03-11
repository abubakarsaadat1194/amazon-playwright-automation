from playwright.sync_api import expect


class SellOnAmazonPage:

    def __init__(self, page):

        self.page = page

        self.home_link = page.get_by_role("link", name="Amazon.de", exact=True)

        self.make_money_link = page.get_by_role(
            "link", name="See More Make Money with Us"
        )

        self.page_title = page.locator("h1")

    def open_make_money_section(self):

        print("Navigating to 'Make Money with Us' section...")

        self.make_money_link.click()

        # sometimes Amazon loads another intermediate page
        if self.make_money_link.count() > 0:
            self.make_money_link.first.click()

        print("✓ 'Make Money with Us' page opened")

    def verify_sell_on_amazon_page(self):

        print("Verifying Sell on Amazon page...")

        expect(self.page_title).to_contain_text(
            "Bauen Sie Ihr Geschäft mit Amazon auf"
        )

        print("✓ Sell on Amazon page loaded successfully\n")