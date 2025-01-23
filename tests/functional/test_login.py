from pages.login_page import LoginPage

def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.enter_username("testuser")
    login_page.enter_password("testpass")
    login_page.click_login()
    # Thêm các kiểm tra sau khi đăng nhập thành công
    assert "Dashboard" in driver.title
