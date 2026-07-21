import time
from os import name

import pytest


from pages.beneficiaryList_page import BeneficiaryListPage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from pages.paymentList_page import PaymentListPage
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
    payment = PaymentListPage(page)

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
    beneficiary.approve_beneficiary(beneficiary_list_id)
    report.stop("Approve Beneficiary List", t)

    # ------------------------------------------------------------------------------------------------------------

    payment_list_id = payment.create_payment(beneficiary_list_id)
    print("Payment List ID: ", payment_list_id)
    payment.approve_payment(payment_list_id)

    # ----------------------------------------------------------------------------------------------------------

    # Generating Performance Report
    report.generate_html()




