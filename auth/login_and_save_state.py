from playwright.sync_api import sync_playwright
from creds import *

def save_auth_state():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()

        page = context.new_page()

        # Open Amazon
        page.goto("https://www.amazon.de/")

        # Accept cookies
        try:
            page.get_by_role("button", name="Accept").click()
        except:
            pass

        # Click Sign in
        page.get_by_role("link", name="Hello, sign in").click()

        # Enter email
        page.get_by_role("textbox", name="Enter mobile number or email").fill(USERNAME)

        page.get_by_role("button", name="Continue").click()

        # Enter password
        page.get_by_role("textbox", name="Password").fill(PASSWORD)

        page.locator("input#signInSubmit").click()

        # Wait until logged in
        page.pause()

        # Save session
        context.storage_state(path="storage_state.json")

        browser.close()


if __name__ == "__main__":
    save_auth_state()