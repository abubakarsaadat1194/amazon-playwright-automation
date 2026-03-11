from playwright.sync_api import expect


class LanguagePage:

    def __init__(self, page):

        self.page = page

        self.language_menu = page.get_by_role(
            "navigation", name="Primary"
        ).get_by_label("Expand to Change Language or")

        self.german_option = page.get_by_role(
            "link", name="Deutsch - DE"
        )

        self.language_panel = page.locator("#nav-flyout-icp")

    def change_language_to_german(self):

        print("Opening language selector...")

        self.language_menu.click()

        print("Selecting German language...")

        self.german_option.click()

        print("✓ Language switched to German")

    def verify_german_language_active(self):

        print("Verifying German language change...")

        expect(self.page).to_have_url("https://www.amazon.de/?language=de_DE")

        print("✓ Language change verified\n")