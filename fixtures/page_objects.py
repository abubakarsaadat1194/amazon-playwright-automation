from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import pytest


@pytest.fixture
def home(page):
    return HomePage(page)


@pytest.fixture
def results(page):
    return SearchResultsPage(page)


@pytest.fixture
def product(page):
    return ProductPage(page)


@pytest.fixture
def cart(page):
    return CartPage(page)