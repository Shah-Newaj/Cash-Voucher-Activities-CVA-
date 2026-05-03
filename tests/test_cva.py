import time

from pages import userRole_page
from pages.login_page import LoginPage
from pages.userRole_page import UserRolePage


def test_cva(page):
    login = LoginPage(page)
    user_role = UserRolePage(page)

    login.load()
    login.login("SuperAdmin", "12345")

    user_role.profile()
    user_role.role()
    user_role.permission()
    user_role.geo()
    user_role.summary()
    user_role.dashboard()
