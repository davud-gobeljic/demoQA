import time
from selenium.webdriver.common.by import By



class Checkbox():

    checkBox_dropdown_id = "item-1"
    button_collapse_xpath = "(//button[@title='Toggle'])[1]"
    first_collappse_arrow_xpath = "//button[@title='Toggle']//*[name()='svg']"
    download_collapse_xpath = "(//*[name()='svg'][@class='rct-icon rct-icon-expand-close'])[3]"
    excel_xpath = "//label[@for='tree-node-excelFile']//span[@class='rct-checkbox']//*[name()='svg']"

    def __init__(self, driver):
        self.driver = driver

    def checkBox_dropdown_click(self):
        self.driver.find_element(By.ID, self.checkBox_dropdown_id).click()

    def buttonCollapse_click(self):
        self.driver.find_element(By.XPATH, self.button_collapse_xpath).click()

    def first_collapse(self):
        self.driver.find_element(By.XPATH, self.first_collappse_arrow_xpath).click()

    def download_collapse(self):
        self.driver.find_element(By.XPATH, self.download_collapse_xpath).click()

    def excel_collapse(self):
        self.driver.find_element(By.XPATH, self.excel_xpath).click()


