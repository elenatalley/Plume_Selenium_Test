"""
2. Using the language of your choice, automate testing a failed login to
http://testphp.vulnweb.com/login.php with the username of rest and a password of rest.
"""
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class TestMainPage:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(4)
        driver.get("hhttp://testphp.vulnweb.com/login.php")
        yield
        time.sleep(3) #explicitly wait
        driver.quit()

    def test_invalid_login(self,test_setup):
        driver.get("http://testphp.vulnweb.com/login.php")
        username = driver.find_element(By.NAME, "uname")
        username.send_keys("rest")
        password = driver.find_element(By.NAME, "pass")
        password.send_keys("rest")
        login = driver.find_element(By.XPATH, '//*[@value="login"]')
        login.click()
        # assert "user info" in driver.title
        assert "login page" in driver.title










