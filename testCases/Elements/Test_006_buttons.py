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

class Test_006_buttons():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()

    def test_buttons(self, setup):
        self.log.info('************* Test_006 *************')
        self.log.info('************* Verifying buttons *************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.elem = Elements(self.driver)
        self.elem.elementsClick()

        self.button = Buttons(self.driver)
        self.button.button_dropdown()
        time.sleep(1)
        self.button.doubleClick_action()
        self.button.rightClick_action()
        self.button.click_just()
        self.rand = RandomGen()

        double_click_confirm_id = 'doubleClickMessage'
        right_click_confirm_id = 'rightClickMessage'
        one_click_confirm_id = 'dynamicClickMessage'

        dbl_clck = self.driver.find_element(By.ID, double_click_confirm_id).text
        rght_clck = self.driver.find_element(By.ID, right_click_confirm_id).text
        one_clck = self.driver.find_element(By.ID, one_click_confirm_id).text

        if 'You have done a double click' == dbl_clck and 'You have done a right click' == rght_clck and 'You have done a dynamic click' == one_clck:
            assert True
            self.driver.close()
            self.log.info('************* Buttons test is PASSED *************')
            self.log.info('- - - - - - - - - -')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     r'/Screenshoots/Test_006_buttons',
                                                     self.rand.random_generator(size=2,
                                                                                chars=string.ascii_lowercase + string.digits) + '_buttons_failed.png'))
            self.driver.close()
            self.log.error('************* Tables Textbox FAILED *************')
            self.log.info('- - - - - - - - - -')
            assert False