import pytest

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


@pytest.mark.parametrize("keyword", [
    "iphone",
    "laptop"
])
def test_click_search_suggestion(page, keyword):

    home = HomePage(page)
    results = SearchResultsPage(page)

    home.navigate()

    print(f"Typing keyword: {keyword}")

    home.search_box.press_sequentially(keyword)

    suggestion = home.click_first_search_suggestion()

    results.verify_results_match_suggestion(suggestion)