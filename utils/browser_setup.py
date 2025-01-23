from selenium import webdriver

def get_driver():
    driver = webdriver.Chrome()  # Đảm bảo chromedriver.exe có trong PATH hoặc chỉ định đường dẫn đầy đủ
    driver.maximize_window()
    return driver
