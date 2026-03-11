from pages.language_page import LanguagePage


def test_change_language_to_german(home, page):

    home.navigate()

    language = LanguagePage(page)

    language.change_language_to_german()

    language.verify_german_language_active()