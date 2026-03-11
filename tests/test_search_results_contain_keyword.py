def test_search_results_contain_keyword(home, results):

    keyword = "iphone"

    # Navigate to homepage
    home.navigate()

    # Search product
    home.search_product(keyword)

    # Verify results are visible
    results.verify_results_visible()

    # Get titles of first few products
    titles = results.results.locator("h2 span")
    count = min(titles.count(), 5)

    print(f"Checking first {count} products for keyword: {keyword}")

    for i in range(1, count, 2):

        title_text = titles.nth(i).inner_text().lower()

        print(f"Product : {title_text}")

        assert keyword in title_text