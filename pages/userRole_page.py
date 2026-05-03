import time

from playwright.sync_api import Page

class UserRolePage(Page):
    def __init__(self, page: Page):
        self.settings = page.locator("//i[@class='fa-solid fa-gear']")
        self.user_role = page.locator("//i[@class='fas fa-user']")
        self.add_btn = page.get_by_role("button", name="Add")
        #------------------------- Profile Page -----------------------------------------
        self.prof_name = page.locator("//div[contains(@class,'col-md-12')]//input[@type='text']")
        self.prof_username = page.locator("(//input[@type='text'])[3]")
        self.prof_email = page.locator("(//input[@type='text'])[4]")
        self.prof_phone = page.locator("//div[contains(@class,'col-md-4')]//input[@type='text']")
        self.prof_active = page.locator("//span[@class='s1']")
        self.next_btn = page.get_by_role("button", name="Next")
        #-------------------- Role Page -------------------------------
        self.u_role = page.locator("//div[contains(@class,'user-list-rf-photo-alt')][normalize-space()='C']")
        #--------------------------- Permission Page --------------------------------------
        self.u_permission = page.locator("//div[@class='rf-permission-selector-header-crud-all']")
        # -------------------------------------------- GEO -----------------------------------------------------
        self.country = page.locator("//div[contains(@class,'geo-title')][normalize-space()='Cashland']")
        self.project_1 = page.locator("//div[normalize-space()='Cash Project V3']")
        self.project_2 = page.locator("//div[normalize-space()='Cashland V3']")
        # -------------------------------------------- Summary ---------------------------------------------
        self.sum_container = page.locator("//div[contains(@title,'Selected UI Permissions')]")
        self.finish_btn = page.get_by_role("button", name="Finish")
        # ---------------------------------------- User Role Dashboard ----------------------------------------
        self.list_container = page.locator("//tr[td[contains(.,'Shah Newaj')]]/td[6]")


    def profile(self):
        self.settings.click()
        self.user_role.click()
        self.add_btn.click()
        self.prof_name.fill("Shah Newaj")
        self.prof_username.fill("Newaj")
        self.prof_email.fill("test@gmail.com")
        self.prof_phone.fill("012345678")
        self.prof_active.click()
        self.next_btn.click()

    def role(self):
        self.u_role.click()
        self.next_btn.click()

    def permission(self):
        # self.u_permission.click() # provide permission manually
        time.sleep(3)
        self.next_btn.click()

    def geo(self):
        self.country.click()
        self.project_1.click()
        self.project_2.click()
        self.next_btn.click()

    def summary(self):
        self.summary_value = self.sum_container.inner_text()
        self.finish_btn.click()
        time.sleep(5)

    def dashboard(self):
        list_value = self.list_container.inner_text()
        #  Removing white space
        self.summary_value = self.summary_value.strip()
        self.list_value = list_value.strip()

        if self.summary_value != self.list_value:
            print(f"❌ FAIL | Expected={self.summary_value}, Actual={self.list_value}")
        else:
            print(f"✅ PASS | Expected={self.summary_value}, Actual={self.list_value}")