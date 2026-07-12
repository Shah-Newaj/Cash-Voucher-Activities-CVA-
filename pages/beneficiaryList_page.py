from playwright.sync_api import Page
import time

class BeneficiaryListPage:
    def __init__(self, page: Page):
        self.page = page
        self.beneficiarylist = page.get_by_text("Beneficiary List Management")
        self.beneficiarylist_overview = page.get_by_role("link", name="Beneficiary List Overview")
        self.create_btn = page.get_by_role("button", name="Create New Beneficiary List")
        self.location3_text = page.locator("(//input[contains(@type,'text')])[5]")
        self.save_btn = page.get_by_role("button", name="Save")
        self.select_all_checkbox = page.locator("//div[contains(@class,'table-rf-check-holder False')]//i[@class='table-rf-check-icon fa-solid fa-check']")
        self.savetobeneficiarylist_btn = page.get_by_role("button", name="Save to Beneficiary List")
        self.sendlistforapproval_btn = page.get_by_role("button", name="Send List for Approval")

    def create_beneficiary(self, location_text):
        self.beneficiarylist.click()
        self.beneficiarylist_overview.click()
        self.create_btn.click()
        self.location3_text.fill(location_text)
        beneficiary_list_id = self.page.locator("(//input[@type='text'])[7]").input_value()
        self.save_btn.click()
        self.select_all_checkbox.click()
        self.savetobeneficiarylist_btn.click()
        self.page.wait_for_load_state("networkidle")
        self.sendlistforapproval_btn.click()
        self.page.wait_for_load_state("networkidle")
        time.sleep(10)

        return beneficiary_list_id



    # def approve_beneficiary(self):
