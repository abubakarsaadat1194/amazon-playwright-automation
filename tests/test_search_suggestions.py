import pytest
from pages.home_page import HomePage


@pytest.mark.parametrize("keyword", [
    "apple",
    "iphone",
    "laptop"
])
def test_search_suggestions(page, keyword):

    home = HomePage(page)

    home.navigate()

    home.search_box.fill(keyword)

    page.wait_for_selector("#nav-flyout-searchAjax")

    home.verify_search_suggestions(keyword)