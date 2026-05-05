import allure
from pages.login_page import LoginPage
from pages.userRole_page import UserRolePage


@allure.feature("CVA User Role")
@allure.story("Create User Role - Happy Path")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify user role creation flow")
def test_cva(page):

    login = LoginPage(page)
    user_role = UserRolePage(page)

    with allure.step("Open application"):
        login.load()

    with allure.step("Login as SuperAdmin"):
        login.login("SuperAdmin", "12345")

    with allure.step("Fill profile information"):
        user_role.profile()

    with allure.step("Assign role"):
        user_role.role()

    with allure.step("Set permissions"):
        user_role.permission()

    with allure.step("Select GEO details"):
        user_role.geo()

    with allure.step("Complete summary"):
        user_role.summary()

    with allure.step("Validate dashboard data"):
        user_role.dashboard()
