def test_open_product(home, results, product):

    # Navigate to homepage
    home.navigate()

    # Search product
    home.search_product("iphone")

    # Verify search results
    results.verify_results_visible()

    # Open first product
    results.open_first_product()

    # Verify product page
    product.verify_product_page()