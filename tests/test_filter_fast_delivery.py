def test_filter_fast_delivery(home, results):

    home.navigate()

    home.search_product("iphone")

    results.verify_results_visible()

    results.apply_fast_delivery_filter()

    results.verify_results_visible()