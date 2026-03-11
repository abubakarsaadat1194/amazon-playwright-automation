def test_filter_rating(home, results):

    home.navigate()

    home.search_product("iphone")

    results.verify_results_visible()

    results.apply_rating_filter()

    results.verify_product_ratings()