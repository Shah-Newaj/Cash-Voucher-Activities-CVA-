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

    # Country & Project Selection
    # Select Country
    t = report.start()

    country = page.locator("div.select-rf[placeholder='Select Country']")
    country.click()
    page.locator(".select-rf-popper").get_by_text("Cashland", exact=True).click()

    page.wait_for_timeout(500)

    report.stop("Select Country", t)
    page.wait_for_load_state("networkidle")
    # Select Project
    t = report.start()

    project = page.locator("div.select-rf[placeholder='Select Project']")
    project.click()
    page.locator(".select-rf-popper").get_by_text("AdminUAT1", exact=True).click()

    page.wait_for_load_state("networkidle")

    report.stop("Select Project", t)

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

    page.get_by_role("button", name="Save").click()

    page.locator(
        "//div[contains(@class,'table-rf-check-holder False')]//i[@class='table-rf-check-icon fa-solid fa-check']"
    ).click()

    page.get_by_role(
        "button",
        name="Save to Beneficiary List"
    ).click()

    page.wait_for_load_state("networkidle")

    report.stop("Create Beneficiary List", t)

    report.generate_html()

    # login.load()
    # login.login("SuperAdmin", "12345")
    #
    # country = page.locator("div.select-rf[placeholder='Select Country']")
    # country.click()
    # page.locator(".select-rf-popper").get_by_text("Cashland", exact=True).click()
    # time.sleep(3)
    # project = page.locator("div.select-rf[placeholder='Select Project']")
    # project.click()
    # page.locator(".select-rf-popper").get_by_text("AdminUAT1", exact=True).click()
    #
    # benef_list_manag = page.get_by_text("Beneficiary List Management")
    # benef_list_manag.click()
    # benef_list_overview = page.get_by_role('link', name="Beneficiary List Overview")
    # benef_list_overview.click()
    # create_benef_list = page.get_by_role('button', name="Create New Beneficiary List")
    # create_benef_list.click()
    # time.sleep(5)
    # loc3 = page.locator("(//input[contains(@type,'text')])[5]")
    # loc3.fill("test")
    # save_btn = page.get_by_role('button', name="Save")
    # save_btn.click()
    # # Select all
    # page.locator("//div[contains(@class,'table-rf-check-holder False')]//i[@class='table-rf-check-icon fa-solid fa-check']").click()
    #
    # # Save
    # save = page.get_by_role('button', name="Save to Beneficiary List")
    # save.click()
    # time.sleep(5)