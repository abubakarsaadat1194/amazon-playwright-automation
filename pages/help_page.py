from playwright.sync_api import expect


class HelpPage:

    def __init__(self, page):

        self.page = page
        self.help_link = page.get_by_role("link", name="Visit the help section")
        self.page_content = page.locator("#a-page")

    def open_help_section(self):

        print("Opening Amazon help section...")

        self.help_link.click()

        print("✓ Help section opened")

    def verify_help_page_loaded(self):

        print("Verifying Help & Customer Service page...")

        expect(self.page_content).to_contain_text("Help and customer service")

        print("✓ Help page loaded successfully\n")