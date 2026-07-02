import time
from os import name

import pytest

from pages.login_page import LoginPage
from pages.performance_report import PerformanceReport

def test_cva_happy_path(page):
    report = PerformanceReport(
        application="CashApp",
        environment="TEST",
        url="https://cashapp-test.savethechildren.net/",
        country="Cashland",
        project="AdminUAT1",
        browser="Chromium"
    )
    login = LoginPage(page)

    # Login
    t = report.start()
    login.load()
    login.login("SuperAdmin", "12345")
    report.stop("Login", t)

    # -------------------------------------------------------------------------------

    # Country & Project Selection
    # Select Country
    t = report.start()

    page.wait_for_timeout(3000)
    country = page.locator("div.select-rf[placeholder='Select Country']")
    country.click()
    page.locator(".select-rf-popper").get_by_text("Cashland", exact=True).click()

    # page.wait_for_timeout(3000)
    time.sleep(2)

    report.stop("Select Country", t)
    page.wait_for_load_state("networkidle")
    # Select Project
    t = report.start()

    project = page.locator("div.select-rf[placeholder='Select Project']")
    project.click()
    page.locator(".select-rf-popper").get_by_text("AdminUAT1", exact=True).click()

    page.wait_for_load_state("networkidle")

    report.stop("Select Project", t)

    # --------------------------------------------------------------------------------

    # Create Beneficiary List
    t = report.start()

    page.get_by_text("Beneficiary List Management").click()

    page.get_by_role(
        "link",
        name="Beneficiary List Overview"
    ).click()

    page.get_by_role(
        "button",
        name="Create New Beneficiary List"
    ).click()

    page.locator("(//input[contains(@type,'text')])[5]").fill("test")

    beneficiary_list_id = page.locator(
        "(//input[@type='text'])[7]"
    ).input_value()

    print(f"Generated ID: {beneficiary_list_id}")

    page.get_by_role("button", name="Save").click()

    page.locator(
        "//div[contains(@class,'table-rf-check-holder False')]//i[@class='table-rf-check-icon fa-solid fa-check']"
    ).click()


    page.get_by_role(
        "button",
        name="Save to Beneficiary List"
    ).click()

    page.wait_for_load_state("networkidle")

    page.get_by_role(
        "button",
        name="Send List for Approval").click()

    page.wait_for_load_state("networkidle")
    time.sleep(10)

    report.stop("Create Beneficiary List", t)

    # ------------------------------------------------------------------------------------------------------------

    # Approve Beneficiary List
    t = report.start()

    page.get_by_role("link", name="Beneficiary List Approval").click()


    time.sleep(10)

    page.locator("//input[@placeholder='Search']").fill(beneficiary_list_id)

    page.keyboard.press("Enter")

    row = page.locator(f"//td[normalize-space()='{beneficiary_list_id}']")

    row.wait_for(state="visible")

    row.click()

    # locator = page.locator(f"//td[normalize-space()='{beneficiary_list_id}']")
    #
    # locator.wait_for(state="visible")
    #
    # locator.click()

    time.sleep(10)
    page.locator("//span[normalize-space()='Approve']").click()

    page.wait_for_load_state("networkidle")
    # time.sleep(10)

    report.stop("Approve Beneficiary List", t)

    # ------------------------------------------------------------------------------------------------------------



    # ----------------------------------------------------------------------------------------------------------

    # Generating Performance Report
    report.generate_html()




