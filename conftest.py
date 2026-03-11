import sys
import os
import pytest
from playwright.sync_api import sync_playwright

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
pytest_plugins = ["fixtures.page_objects"]

@pytest.fixture(scope="session")
def browser_context():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            storage_state="storage_state.json"
    #record_video_dir="videos/"
        )

        yield context
        context.close()
        browser.close()


@pytest.fixture()
def page(browser_context):

    page = browser_context.new_page()

    yield page

    page.close()

# Screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = f"screenshots/{item.name}.png"

            page.screenshot(path=screenshot_path)

            print(f"\nScreenshot saved: {screenshot_path}")