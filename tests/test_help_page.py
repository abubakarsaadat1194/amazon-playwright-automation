def test_open_help_page(home, page, results):

    from pages.help_page import HelpPage

    home.navigate()
    home.search_product("iphone")
    
    help_page = HelpPage(page)

    

    help_page.open_help_section()

    help_page.verify_help_page_loaded()