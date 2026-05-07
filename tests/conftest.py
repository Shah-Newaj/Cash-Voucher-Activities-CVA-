import os
import time

import pytest
import allure
from playwright.sync_api import sync_playwright

import os
import allure
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":

        page = item.funcargs.get("page", None)

        if page:

            # ---------------- SCREENSHOT ----------------
            if rep.failed:
                screenshot = page.screenshot()

                allure.attach(
                    screenshot,
                    name="failure-screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            # ---------------- VIDEO ----------------
            video_path = page.video.path()

            if os.path.exists(video_path):

                allure.attach.file(
                    video_path,
                    name="execution-video",
                    attachment_type=allure.attachment_type.WEBM
                )

@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            record_video_dir="videos/"
        )

        page = context.new_page()

        yield page

        page.close()
        context.close()
        browser.close()