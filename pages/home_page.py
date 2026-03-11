from playwright.sync_api import expect


class HomePage:

    def __init__(self, page):
        self.page = page
        self.search_box = page.get_by_placeholder("Search Amazon.de")
        self.logo = page.locator("#nav-logo-sprites")
        self.cart_icon = page.locator("span.nav-cart-icon")
        self.search_suggestions = page.locator("#nav-flyout-searchAjax")

    def navigate(self):

        print("Navigating to Amazon homepage...")
        self.page.goto("https://www.amazon.de")

        try:
            print("Handling cookie popup if present...")
            self.page.get_by_role("button", name="Accept").click()
            print("Cookie popup accepted.")
        except:
            print("No cookie popup found.")

        print("Verifying homepage elements...")

        # Assertions
        expect(self.page).to_have_url("https://www.amazon.de/")
        print("✓ URL verification passed.")

        expect(self.logo).to_be_visible()
        print("✓ Amazon logo is visible.")

        expect(self.search_box).to_be_visible()
        print("✓ Search box is visible.")

        expect(self.cart_icon).to_be_visible()
        print("✓ Cart icon is visible.")

        print("Homepage loaded successfully.\n")

    def search_product(self, product):

        print(f"Searching for product: {product}")
        
        self.search_box.press_sequentially(product)
        print("Search text entered.")

        self.page.keyboard.press("Enter")
        print("Search submitted.\n")
    def verify_search_suggestions(self, keyword):

        print(f"Verifying search suggestions for keyword: {keyword}")

        # Wait until suggestions are populated
        self.page.wait_for_function(
            "document.querySelector('#nav-flyout-searchAjax') && "
            "document.querySelector('#nav-flyout-searchAjax').innerText.length > 0"
        )

        suggestion_block = self.search_suggestions.first.inner_text()

        suggestions = suggestion_block.split("\n")

        # Clean suggestions
        suggestions = [
            s.strip().lower()
            for s in suggestions
            if s.strip() and not s.lower().startswith("prefix")
        ]

        print(f"Total suggestions found: {len(suggestions)}")

        match_count = 0

        for suggestion in suggestions:
            print(f"Suggestion: {suggestion}")

            if suggestion.startswith(keyword.lower()):
                match_count += 1

        assert match_count > 0, f"No suggestions start with '{keyword}'"

        print("✓ Search suggestions contain the keyword prefix.\n")
    def click_first_search_suggestion(self):

        print("Waiting for search suggestions...")

        self.page.wait_for_selector("#nav-flyout-searchAjax")

        suggestion = self.page.locator("#nav-flyout-searchAjax div[role='button']").first

        suggestion_text = suggestion.inner_text().split("\n")[0].strip()

        print(f"Clicking suggestion: {suggestion_text}")

        suggestion.click()

        return suggestion_text