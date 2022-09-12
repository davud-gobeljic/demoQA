import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class RadioBTN():

    radioBtn_dropdown_id = "item-2"
    impressive_radioBtn_xpath = "//label[normalize-space()='Impressive']"
    is_sel_BTNimpressiveRadio_id = 'impressiveRadio'

    def __init__(self, driver):
        self.driver = driver

    def radio_dropdown(self):
        self.driver.find_element(By.ID, self.radioBtn_dropdown_id).click()

    def is_selected_BTN(self):
        status = self.driver.find_element(By.ID, self.is_sel_BTNimpressiveRadio_id).is_selected()
        if status == False:
            print("\nImpressive radio button is not selected")
        else:
            print("\nImpressive radio button is selected")

    def clickImpressive_radioBtn(self):
        self.driver.find_element(By.XPATH, self.impressive_radioBtn_xpath).click()
