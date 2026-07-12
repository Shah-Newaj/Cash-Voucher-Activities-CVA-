import time
from os import name

import pytest

from pages.beneficiaryList_page import BeneficiaryListPage
from pages.dashboard_page import Dashboard
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
    dashboard = Dashboard(page)
    beneficiary = BeneficiaryListPage(page)

    # Login
    t = report.start()
    login.load()
    login.login("SuperAdmin", "Welcome@2")
    report.stop("Login", t)

    # -------------------------------------------------------------------------------

    # Country & Project Selection
    t = report.start()
    page.wait_for_timeout(3000)
    dashboard.select_country()
    page.wait_for_timeout(3000)
    dashboard.select_project()
    page.wait_for_load_state("networkidle")
    report.stop("Select Country & Project", t)

    # --------------------------------------------------------------------------------

    # Create Beneficiary List
    t = report.start()

    beneficiary_list_id = beneficiary.create_beneficiary("test")
    print("Beneficiary List ID: ", beneficiary_list_id)

    report.stop("Create Beneficiary List", t)

    # ------------------------------------------------------------------------------------------------------------

    # Approve Beneficiary List
    t = report.start()

    page.get_by_role("link", name="Beneficiary List Approval").click()

    time.sleep(5)

    page.locator("//input[@placeholder='Search']").fill(beneficiary_list_id)
    page.keyboard.press("Enter")
    time.sleep(5)
    row = page.locator("//tbody//tr//td[2]")
    row.wait_for(state="visible")
    row.click()

    # locator = page.locator(f"//td[normalize-space()='{beneficiary_list_id}']")
    # locator = page.getByRole('link', name="AdminUAT1/UN OC/test/12Jul20/beneficiary_list_id")
    # locator.wait_for(state="visible")
    # locator.click()

    time.sleep(10)
    approve_btn = page.locator("//span[normalize-space()='Approve']")
    approve_btn.click()

    page.wait_for_load_state("networkidle")
    # time.sleep(10)

    report.stop("Approve Beneficiary List", t)

    # ------------------------------------------------------------------------------------------------------------



    # ----------------------------------------------------------------------------------------------------------

    # Generating Performance Report
    report.generate_html()




