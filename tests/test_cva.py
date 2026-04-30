from pages.login_page import LoginPage


def test_cva(page):
    login = LoginPage(page)

    login.load()
    login.login("SuperAdmin", "12345")
