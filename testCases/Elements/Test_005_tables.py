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

class Test_005_tables():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()
    firstname = 'Davud'
    lastname = 'Gobeljic'
    email = 'davud@live.com'
    age = '32'
    salary = '5000'
    department = 'QA'

    table_grid_xpath = "//div[@role='grid']"

    def test_005_tables(self, setup):
        self.log.info('************* Test_005 *************')
        self.log.info('************* Verifying tables *************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.elem = Elements(self.driver)
        self.elem.elementsClick()
        self.rand = RandomGen()

        self.tables = Tables(self.driver)
        self.tables.webtables_dropdown()
        self.tables.addBTN()
        self.tables.setFirstName(self.firstname)
        self.tables.setLastName(self.lastname)
        self.tables.setEmail(self.email)
        self.tables.setAge(self.age)
        self.tables.setSalary(self.salary)
        self.tables.setDepartment(self.department)
        self.tables.submitBTN()
        self.tables.deleteRecord()

        table = self.driver.find_elements(By.XPATH, self.table_grid_xpath)
        data = []
        for r in table:
            # print(r.text, end=" ")
            data.append(r.text)

        for x in range(len(data)):
            dbol = (data[x])
            if "Davud" in dbol:
                assert True
                self.driver.close()
                self.log.info('************* Tables test is PASSED *************')
                self.log.info('- - - - - - - - - -')
            else:
                self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                         r'/Screenshoots/Test_005_tables',
                                                         self.rand.random_generator(size=2,
                                                                                    chars=string.ascii_lowercase + string.digits) + '_tables_failed.png'))
                self.driver.close()
                self.log.error('************* Tables Textbox FAILED *************')
                self.log.info('- - - - - - - - - -')
                assert False


