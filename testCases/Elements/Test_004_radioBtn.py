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
from pageObjects.radioButton_pageObject import RadioBTN

class Test_004_radioBtn():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()


    def test_004_radioBtn(self, setup):
        self.log.info('************* Test_004 *************')
        self.log.info('************* Verifying Radio Button *************')
        self.driver = setup
        self.driver.get(self.baseURL)

        self.elem = Elements(self.driver)
        self.elem.elementsClick()
        self.radioBTN = RadioBTN(self.driver)
        self.radioBTN.radio_dropdown()
        self.radioBTN.clickImpressive_radioBtn()
        self.radioBTN.is_selected_BTN()
        self.rand = RandomGen()
        yesRadio_BTN = 'yesRadio'

        selec = self.driver.find_element(By.ID, yesRadio_BTN).is_selected()

        if not selec:
            assert True
            self.driver.close()
            self.log.info('************* Radio Button test is PASSED *************')
            self.log.info('- - - - - - - - - -')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     r'/Screenshoots/Test_004_radioBtn',
                                                     self.rand.random_generator(size=2,
                                                                                chars=string.ascii_lowercase + string.digits) + '_radioBtn_failed.png'))
            self.driver.close()
            self.log.error('************* Checkbox Textbox FAILED *************')
            self.log.info('- - - - - - - - - -')
            assert False


