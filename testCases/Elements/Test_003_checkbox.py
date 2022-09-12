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
from pageObjects.checkBox_pageObject import Checkbox
from pageObjects.elements_pageObject import Elements

class Test_003_checkbox():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()

    def test_checkbox(self, setup):
        self.log.info('************* Test_003 *************')
        self.log.info('************* Verifying Checbox *************')
        self.driver = setup
        self.driver.get(self.baseURL)

        self.elem = Elements(self.driver)
        self.rand = RandomGen()
        self.elem.elementsClick()

        self.checkbox = Checkbox(self.driver)
        self.checkbox.checkBox_dropdown_click()
        self.checkbox.buttonCollapse_click()
        self.checkbox.download_collapse()
        self.checkbox.excel_collapse()
        self.msg = self.driver.find_element(By.TAG_NAME, 'body')
        print(self.msg.text)
        exce = "excelFile"

        if exce in self.msg.text:
            assert True
            self.driver.close()
            self.log.info('************* Checkbox test is PASSED *************')
            self.log.info('- - - - - - - - - -')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     r'/Screenshoots/Test_003_Checkbox',
                                                     self.rand.random_generator(size=2,
                                                                                chars=string.ascii_lowercase + string.digits) + '_Checkbox_failed.png'))
            self.driver.close()
            self.log.error('************* Checkbox Textbox FAILED *************')
            self.log.info('- - - - - - - - - -')
            assert False