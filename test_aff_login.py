# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAffLogin(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
    
    def test_aff_login(self):
        wd = self.wd
        wd.get("https://affiliate.hoqu.com/")
        wd.find_element_by_xpath("//div[@id='application']/div/div[2]/div[3]").click()
        wd.find_element_by_xpath("//div[@id='application']/div/div[2]/div[4]/div/div/div/a/div/div/div/span").click()
        wd.find_element_by_xpath("//input[@value='Demo Affiliate']").click()
        wd.find_element_by_xpath("//input[@value='Demo Affiliate 1']").clear()
        wd.find_element_by_xpath("//input[@value='Demo Affiliate 1']").send_keys("Demo Affiliate 1")
        wd.find_element_by_xpath("//div[@id='main-layout']/div/div[2]/div[2]/div/div/div[2]/form/div[8]/button/span").click()
        wd.find_element_by_xpath("//div[@id='application']/div/div[2]/a/div/div").click()
        wd.find_element_by_xpath("//div[@id='application']/header/div[2]/button/span/div").click()
        wd.find_element_by_xpath("//div[2]/ul/li[2]/span").click()
    
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