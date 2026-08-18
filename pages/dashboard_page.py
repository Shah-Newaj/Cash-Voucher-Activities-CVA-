from playwright.sync_api import Page

class Dashboard:
    def __init__(self, page: Page):
        self.page = page
        self.domain_drp = page.locator("//span[text()='Domain:']/following::span[text()='Select'][1]")
        self.domain = page.locator(".select-rf-popper").get_by_text("sci-co-niger", exact=True)  # change domain name here if required
        self.country_drp = page.locator("//span[text()='Country:']/following::span[text()='Select'][1]")
        self.country = page.locator(".select-rf-popper").get_by_text("Niger CVA", exact=True) #change country name here if required
        self.project_drp = page.locator("//span[text()='Project:']/following::span[text()='Select'][1]")
        self.project = page.locator(".select-rf-popper").get_by_text("BMZ RESA Training", exact=True) #change project name here if required
        self.login_btn = page.get_by_role("button", name="Login")

    def select_country(self):
        self.country_drp.click()
        self.country.click()

    def select_project(self):
        self.project_drp.click()
        self.project.click()