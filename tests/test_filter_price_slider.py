def test_filter_price_slider(home, results):

    home.navigate()

    home.search_product("iphone")

    results.verify_results_visible()

    results.apply_price_slider(35, 116)

    results.verify_prices_in_range(35, 116)