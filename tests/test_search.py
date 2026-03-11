def test_search_product(home, results):

    # Navigate to homepage
    home.navigate()

    # Search for a product
    home.search_product("iphone")

    # Verify search results are visible
    results.verify_results_visible()