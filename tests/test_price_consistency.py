def test_price_consistency(home, results, product):

    home.navigate()

    home.search_product("iphone")

    results.verify_results_visible()

    # Capture price from search results
    search_price = results.get_first_product_price()

    print(f"Price in search results: {search_price}")

    results.open_first_product()

    # Capture price from product page
    product_price = product.get_product_price()

    print(f"Price on product page: {product_price}")

    assert search_price == product_price