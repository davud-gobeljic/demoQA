import time
import pytest
import selenium.webdriver.firefox.firefox_binary
from selenium import webdriver
import os
import string
import random
from Utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from Utilities.customLogger import LogGen
from pageObjects.randomGenerator import RandomGen
from pageObjects.elements_pageObject import Elements
from pageObjects.tables_pageObejcts import Tables
from pageObjects.buttons_pageObject import Buttons
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.links_pageObject import Links

class Test_007_links():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()



    def test_links(self, setup):
        self.log.info('************* Test_007 *************')
        self.log.info('************* Verifying links *************')
        self.driver = setup
        self.driver.get(self.baseURL)

        self.elem = Elements(self.driver)
        self.elem.elementsClick()

        self.link = Links(self.driver)
        self.link.links_dropdown()

        all_links_xpath = "//div[@id='linkWrapper'] //a"
        links_all = self.driver.find_elements(By.XPATH, all_links_xpath)

        unathorized_xpath = "//a[@id='unauthorized']"
        unathorized = self.driver.find_element(By.XPATH, unathorized_xpath)

        print(len(all_links_xpath))

        for link in links_all:
            print(link.text)
            if link.text == "Home":
                link.click()
            elif unathorized.text == 'Unauthorized':
                unathorized.click()

        wind_handle = self.driver.window_handles
        print("\n\nTotal windows open: ", len(wind_handle))

        for single_window in wind_handle:
            self.driver.switch_to.window(single_window)
            print(self.driver.title)
        