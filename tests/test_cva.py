import pytest
import allure

from utils.excel_utils import ExcelUtils
from pages.login_page import LoginPage
from pages.userRole_page import UserRolePage


test_data = ExcelUtils.get_data(
    "data/users.xlsx",
    "Users"
)


@pytest.mark.parametrize(
    "full_name, username, email, phone, role, image",
    test_data
)

@allure.feature("CVA User Role")
@allure.story("Create User Role - Happy Path")
@allure.severity(allure.severity_level.CRITICAL)
def test_cva(page, full_name, username, email, phone, role, image):

    allure.dynamic.title(f"Create User: {full_name}")

    login = LoginPage(page)
    user_role = UserRolePage(page)

    with allure.step("Open application"):
        login.load()

    with allure.step("Login as SuperAdmin"):
        login.login("SuperAdmin", "12345")

    with allure.step(f"Create user: {full_name}"):

        user_role.profile(
            full_name,
            username,
            email,
            phone,
            image
        )

    with allure.step("Assign role"):
        user_role.role(role)

    with allure.step("Set permissions"):
        user_role.permission()

    with allure.step("Select GEO details"):
        user_role.geo()

    with allure.step("Complete summary"):
        user_role.summary()

    with allure.step("Validate dashboard data"):
        user_role.dashboard(full_name)