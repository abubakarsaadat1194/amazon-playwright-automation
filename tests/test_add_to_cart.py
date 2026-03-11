def test_add_product_to_cart(home, results, product, cart):

    home.navigate()

    home.search_product("iphone")

    results.verify_results_visible()

    results.open_first_product()

    product.verify_product_page()

    product.add_product_to_cart()

    cart.open_cart()

    cart.verify_cart_visible()

    