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


class Test_002_elements_textbox():
    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()
    username = 'Davud Gobeljic'
    email = 'davud.gobeljic@gmail.com'
    currentAdress = 'Sarajevo, Hendek 27'
    permanentAdress = 'Sarajevo, Hendek 27'

    def test_element_textbox(self, setup):
        self.log.info('************* Test_002 *************')
        self.log.info('************* Verifying Elements Textbox*************')
        self.driver = setup
        self.driver.get(self.baseURL)

        self.elem = Elements(self.driver)
        self.elem.elementsClick()
        self.elem.textBox_click()
        self.elem.userName_input(self.username)
        self.elem.email_input(self.email)
        self.elem.current_adress_input(self.currentAdress)
        self.elem.permanent_adress_input(self.permanentAdress)
        self.elem.submitBTN_click()
        self.rand = RandomGen()

        self.msg = self.driver.find_elements(By.TAG_NAME, "p")
        n = []
        for ons in self.msg:
            n.append(ons.text)

        print(n[1])
        logEmail = n[1]

        # if 'Email:davud.gobeljic@gmail.com' == logEmail:
        if self.email in logEmail:
            assert True
            self.driver.close()
            self.log.info('************* Elements test is PASSED *************')
            self.log.info('- - - - - - - - - -')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     r'/Screenshoots/Test_002_Elements_TextBox',
                                                     self.rand.random_generator(size=2,
                                                                                chars=string.ascii_lowercase + string.digits) + '_elementsTextbox_failed.png'))
            self.driver.close()
            self.log.error('************* Elements Textbox FAILED *************')
            self.log.info('- - - - - - - - - -')
            assert False