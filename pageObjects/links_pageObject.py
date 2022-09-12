from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Links():

    links_dropdown_id = "item-5"

    def __init__(self, driver):
        self.driver = driver

    def links_dropdown(self):
        self.driver.find_element(By.ID, self.links_dropdown_id).click()

