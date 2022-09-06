import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Elements():

    element_main_xpath = "//body/div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div[@class='category-cards']/div[1]"
    textBox_id = 'item-0'
    fullname_id = 'userName'
    email_id = 'userEmail'
    currentAdress_id = 'currentAddress'
    permanentAdress_id = 'permanentAddress'
    submitBTN_id = 'submit'

    def __init__(self, driver):
        self.driver = driver

    def elementsClick(self):
        self.driver.find_element(By.XPATH, self.element_main_xpath).click()

    def textBox_click(self):
        self.driver.find_element(By.ID, self.textBox_id).click()

    def userName_input(self, fullname):
        self.driver.find_element(By.ID, self.fullname_id).send_keys(fullname)

    def email_input(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def current_adress_input(self, currentAdress):
        self.driver.find_element(By.ID, self.currentAdress_id).send_keys(currentAdress)

    def permanent_adress_input(self, permAdress):
        self.driver.find_element(By.ID, self.permanentAdress_id).send_keys(permAdress)

    def submitBTN_click(self):
        self.driver.find_element(By.ID, self.submitBTN_id).click()