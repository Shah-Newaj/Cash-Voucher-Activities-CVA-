import os
import time

import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    page = item.funcargs.get("page", None)

    # ---------------- SCREENSHOT ----------------
    if rep.when == "call" and rep.failed:

        if page:
            screenshot = page.screenshot()

            allure.attach(
                screenshot,
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG
            )

    # ---------------- SAVE VIDEO PATH ----------------
    if rep.when == "call" and page and page.video:

        item.video_path = page.video.path()

    # ---------------- ATTACH FINALIZED VIDEO ----------------
    if rep.when == "teardown":

        video_path = getattr(item, "video_path", None)

        if video_path and os.path.exists(video_path):

            # 🔥 Wait for Playwright encoding finalize
            time.sleep(3)

            allure.attach.file(
                video_path,
                name=f"{item.name}-video",
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