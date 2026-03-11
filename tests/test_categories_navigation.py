import pytest
from pages.categories_page import CategoriesPage


@pytest.mark.parametrize("subcategory", [
    "Books",
    "Kindle Books (German)",
    "Textbooks"
])
def test_category_navigation(page, subcategory):

    categories = CategoriesPage(page)

    page.goto("https://www.amazon.de")

    categories.open_menu()

    categories.open_category("Books")

    categories.click_subcategory(subcategory)