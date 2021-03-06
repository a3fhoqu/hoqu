# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
    
    def test_login_logout(self):
        wd = self.wd
        self.open_login_page(wd)
        self.login_by_affiliate(wd)
        self.open_news_by_affiliate(wd)
        self.logout_by_affiliate(wd)

    def logout_by_affiliate(self, wd):
        wd.find_element_by_xpath("//div[@id='application']/header/div[2]/button/span/div").click()
        wd.find_element_by_xpath("//li[2]/span").click()

    def open_news_by_affiliate(self, wd):
        wd.find_element_by_xpath("//div[@id='application']/div/div[5]/a/div/div/div/span").click()

    def login_by_affiliate(self, wd):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("demoaffiliate@hoqu.com")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("a0b0c0d0ef")
        wd.find_element_by_xpath("//div[@id='app']/div[2]/section/div/div/div/form/button/span/b").click()

    def open_login_page(self, wd):
        wd.get("https://login.hoqu.com/login")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
