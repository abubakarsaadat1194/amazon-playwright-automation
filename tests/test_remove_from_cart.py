def test_remove_product_from_cart(home, results, product, cart):

    # Navigate to homepage
    home.navigate()

    # Search product
    home.search_product("samsung")

    # Verify results
    results.verify_results_visible()

    # Open first product
    results.open_first_product()

    # Add product to cart
    product.add_product_to_cart()

    # Open cart
    cart.open_cart()

    # Remove item from cart
    cart.delete_item()