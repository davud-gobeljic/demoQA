import time
from selenium.webdriver.common.by import By

class Tables():

    webtables_dropdown_id = "item-3"
    addBTN_id = 'addNewRecordButton'
    firstname_id = 'firstName'
    lastname_id = 'lastName'
    email_id = 'userEmail'
    age_id = 'age'
    salary_id = 'salary'
    department_id = 'department'
    submit_id = 'submit'
    delete_record = 'delete-record-2'


    def __init__(self, driver):
        self.driver = driver

    def webtables_dropdown(self):
        self.driver.find_element(By.ID, self.webtables_dropdown_id).click()

    def addBTN(self):
        self.driver.find_element(By.ID, self.addBTN_id).click()

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.firstname_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.lastname_id).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def setAge(self, age):
        self.driver.find_element(By.ID, self.age_id).send_keys(age)

    def setSalary(self, salary):
        self.driver.find_element(By.ID, self.salary_id).send_keys(salary)

    def setDepartment(self, department):
        self.driver.find_element(By.ID, self.department_id).send_keys(department)

    def submitBTN(self):
        self.driver.find_element(By.ID, self.submit_id).click()

    def deleteRecord(self):
        self.driver.find_element(By.ID, self.delete_record).click()