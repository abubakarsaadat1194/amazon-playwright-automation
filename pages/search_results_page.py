from playwright.sync_api import expect


class SearchResultsPage:

    def __init__(self, page):

        self.page = page

        # Search results container
        self.results = page.locator('[data-component-type="s-search-result"]')

        # Product titles
        self.product_titles = page.locator(
            '[data-component-type="s-search-result"] h2 span'
        )

    def verify_results_visible(self):

        print("Waiting for search results to become visible...")

        expect(self.results.first).to_be_visible(timeout=10000)

        print("✓ Search results are visible.\n")

    def open_first_product(self):

        print("Opening first product from search results...")

        first_product = self.results.locator("h2 span").nth("1")

        first_product.click()

        print("✓ Product page opened.\n")

    def verify_results_match_suggestion(self, suggestion):

        print(f"Verifying results match suggestion: {suggestion}")

        self.page.wait_for_selector('[data-component-type="s-search-result"]')

        titles = self.product_titles.all_inner_texts()

        match_count = 0

        for title in titles:

            print(f"Result: {title}")

            if suggestion.lower().split()[0] in title.lower():
                match_count += 1

        assert match_count > 0, "Search results do not match suggestion"

        print("✓ Search results match suggestion\n")
    def get_first_product_price(self):

        price = self.page.locator(
            '[data-component-type="s-search-result"] span.a-price-whole'
        ).first.inner_text()

        return price

    def apply_fast_delivery_filter(self):

        print("Applying fast delivery filter...")

        self.page.get_by_role("link", name="Apply the filter Get It").click()

        self.page.wait_for_load_state("networkidle")
    def apply_condition_filter_new(self):

        print("Applying condition filter: New")

        self.page.get_by_role("link", name="Apply the filter New to").click()

        self.page.wait_for_load_state("networkidle")
   
    def apply_price_slider(self, min_price, max_price):

        print(f"Applying price slider filter: {min_price}-{max_price}")

        # scroll to filters
        self.page.mouse.wheel(0, 1500)

        min_slider = self.page.get_by_role("slider", name="Minimum price")
        max_slider = self.page.get_by_role("slider", name="Maximum price")

        min_slider.wait_for(state="visible")
        max_slider.wait_for(state="visible")

        # capture first product before filtering
        first_product = self.page.locator('[data-component-type="s-search-result"]').first
        old_product = first_product.inner_text()

        # move minimum slider
        min_slider.fill(str(min_price))

        # wait for product refresh
        self.page.wait_for_function(
    """([selector, oldText]) => {
        const el = document.querySelector(selector);
        return el && el.innerText !== oldText;
    }""",
    arg=['[data-component-type="s-search-result"]', old_product]
)

        # capture new first product
        old_product = first_product.inner_text()

        # move maximum slider
        max_slider.fill(str(max_price))

        # wait again for refresh
        self.page.wait_for_function(
    """([selector, oldText]) => {
        const el = document.querySelector(selector);
        return el && el.innerText !== oldText;
    }""",
    arg=['[data-component-type="s-search-result"]', old_product]
)

        print("✓ Price slider applied and results refreshed\n")
   
    def verify_prices_in_range(self, min_price, max_price):

        products = self.page.locator('[data-component-type="s-search-result"]')

        count = products.count()

        for i in range(count):

            product = products.nth(i)

            # skip sponsored products
            if product.locator("text=Sponsored").count() > 0:
                continue

            price_locator = product.locator("span.a-price-whole")

            if price_locator.count() == 0:
                continue

            price = price_locator.first.inner_text()

            price = price.replace(".", "").strip()

            try:
                price = int(price)
            except:
                continue

            print(f"Product price: {price}")

            assert min_price <= price <= max_price, \
                f"Price {price} outside range {min_price}-{max_price}"

        print("✓ All non-sponsored products fall within selected range\n")

    def apply_rating_filter(self):

        print("Applying rating filter: 4 Stars & Up")

        rating_filter = self.page.get_by_role(
            "link", name="Apply the filter 4 Stars & Up"
        )

        rating_filter.click()

        print("✓ Rating filter applied")

        # wait for results to refresh
        self.page.wait_for_timeout(3000)
    def verify_product_ratings(self):

        print("Verifying product ratings are 4 stars and above")

        ratings = self.page.locator(
            '[data-component-type="s-search-result"] span.a-icon-alt'
        ).all_inner_texts()

        for rating in ratings:

            if "out of" not in rating:
                continue

            rating_value = float(rating.split(" ")[0])

            print(f"Product rating: {rating_value}")

            assert rating_value >= 4.0, \
                f"Rating {rating_value} is below 4 stars"

        print("✓ All ratings are 4 stars and above\n")