def test_filter_condition_new(home, results):

    home.navigate()

    home.search_product("iphone")

    results.apply_condition_filter_new()

    results.verify_results_visible()