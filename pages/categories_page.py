from playwright.sync_api import expect


class CategoriesPage:

    def __init__(self, page):
        self.page = page
        self.hamburger = page.get_by_role("button", name="Open All Categories Menu")

    def open_menu(self):
        self.hamburger.click()
        self.page.locator(".hmenu-visible").first.wait_for()

    def open_category(self, category):

        panel = self.page.locator(".hmenu-visible").last

        panel.get_by_role(
            "button",
            name=category,
            exact=True
        ).click()

    def click_subcategory(self, name):

        panel = self.page.locator(".hmenu-visible").last

        panel.get_by_role(
            "link",
            name=name,
            exact=True
        ).click()
    def open_best_sellers(self):
        self.page.get_by_role("link", name="Best Sellers").click()


    def verify_beauty_best_sellers(self):
        assert self.page.get_by_role("heading", name="Best Sellers in Beauty").is_visible()


    def select_department(self, department):
        self.page.get_by_label("Select the department you").select_option(department)