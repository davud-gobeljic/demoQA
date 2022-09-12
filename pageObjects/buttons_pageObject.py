from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Buttons():

    button_dropdown_id = "item-4"
    double_click_btn_id = 'doubleClickBtn'
    right_click_btn_id = "rightClickBtn"
    click_me_btn_xpath = "(//button[normalize-space()='Click Me'])[1]"


    def __init__(self, driver):
        self.driver = driver

    def button_dropdown(self):
        self.driver.find_element(By.ID, self.button_dropdown_id).click()

    def doubleClick_action(self):
        double_click = self.driver.find_element(By.ID, self.double_click_btn_id)
        ac_obj = ActionChains(self.driver)
        ac_obj.double_click(double_click).perform()

    def rightClick_action(self):
        right_click = self.driver.find_element(By.ID, self.right_click_btn_id)
        ac_obj = ActionChains(self.driver)
        ac_obj.context_click(right_click).perform()

    def click_just(self):
        click_me = self.driver.find_element(By.XPATH, self.click_me_btn_xpath)
        ac_obj = ActionChains(self.driver)
        ac_obj.click(click_me).perform()

    def clck(self):
        self.driver.find_element(By.XPATH, self.click_me_btn_xpath).click()


