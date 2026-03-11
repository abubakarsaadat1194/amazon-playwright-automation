from pages.sell_on_amazon_page import SellOnAmazonPage


def test_open_sell_on_amazon(home, page):

    home.navigate()

    sell_page = SellOnAmazonPage(page)

    sell_page.open_make_money_section()

    sell_page.verify_sell_on_amazon_page()